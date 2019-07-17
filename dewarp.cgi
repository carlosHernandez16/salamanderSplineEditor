# Here goes the dewarp program written by John in C but for now there is this TCL script for placeholder purposes

#!/usr/bin/tclsh

puts "Content-type: text/plain\n"

set env(HOME) /Library/Webserver/CGI-Executables

set input [read stdin]

if [info exists env(QUERY_STRING)] {
  set counter 0

  for {set i 0} {$i < [string length $input]} {incr i} {
    if {[string index $input $i] eq "+"} {
      set fileIMG [string range $input 0 [expr $counter - 1]]
      puts $fileIMG
      break
    } else {
        incr counter
      }
  }
}
