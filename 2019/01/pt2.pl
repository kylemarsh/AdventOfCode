#! /usr/bin/env perl

my $total = 0;
for (<>) {
    $total += rocket($_);
}
print "$total\n";


sub rocket {
    my $mass = shift;
    my $fuel = (int($mass / 3) - 2);
    #print "mass $mass requires $fuel fuel\n";
    return 0 if $fuel <= 0;
    return $fuel + rocket($fuel);
}
