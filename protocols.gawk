#!/usr/bin/gawk -f

BEGIN { FS = "[<>]" }
(/<record/) { v=n=d="" }
(/<value/) { v=$3 }
(/<name/ && $3!~/ /) { n=$3 }
(/<description/) { d=$3 }
(/<\/record/ && n && v!="") { printf "%-16s %3i %-16s # %s\n", tolower(n),v,n,d }
