const std = @import("std");

pub fn main() !void {

    // Creates a general purpose memory allocator (will allocate a lot of memeory)

    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const alloc = gpa.allocator();

    // Gets commandline arguments and places them into the gpa allocator

    const args = try std.process.argsAlloc(alloc);

    // Will execute at the end of main's scope

    defer std.process.argsFree(alloc, args);

    // Opens the file

    const input_file = args[1];
    const file = try std.fs.cwd().openFile(input_file, .{});

    // Grabs the file's size which we'll use as the max size for the reader

    const meta = try file.metadata();
    const file_size = meta.size();

    // Will close the file at the end of main's scope

    defer file.close();

    // Reads the file

    var buffered_reader = std.io.bufferedReader(file.reader());
    const reader = buffered_reader.reader();

    // Grabs a reader object that represents the file's contents

    const contents = try reader.readAllAlloc(alloc, file_size);

    // Will free contents at the end of main's scope

    defer alloc.free(contents);

    // Creates a hash map using our already existing allocator

    var map = std.StringArrayHashMap(usize).init(alloc);
    defer map.clearAndFree();

    // Tokenizes the contents of the file w/o consecutive deliminators (takes care of whitespace)

    var words = std.mem.tokenizeAny(u8, contents, " \n");

    // Will get the total word count

    var total_words: u64 = 0;

    while (words.next()) |this_word| {
        const has_word = map.contains(this_word);

        // This switch adds keys that aren't in the map already with their value set to 1 or increases already
        // existing key's values by 1

        switch (has_word) {
            true => {

                // Grabs a pointer to the key-value pair

                const value = map.getEntry(this_word).?;

                // Deferences the value pointer and adds 1 to it

                value.value_ptr.* += 1;
            },
            false => try map.putNoClobber(this_word, 1),
        }
    }

    // Creates an interator over the hashmap

    var iterator = map.iterator();

    // Need at standard output writer to print

    const stdout = std.io.getStdOut().writer();

    // Prints each kv pair in the hashmap if their value is greater than 1 and adds their count to the total word count

    while (iterator.next()) |the_word| {
        total_words += the_word.value_ptr.*;

        if (the_word.value_ptr.* > 1) try stdout.print("{s} {any}\n", .{ the_word.key_ptr.*, the_word.value_ptr.* }) else continue;
    }

    try stdout.print("\n{s} {any}\n", .{ args[1], total_words });
}
