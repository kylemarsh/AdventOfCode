#! /usr/bin/env perl

$total = 0;
for (<>) {
    $total += (int($_ / 3) - 2);
}
print "$total\n";

