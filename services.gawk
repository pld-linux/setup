#!/usr/bin/gawk -f

BEGIN { print "# service-name     port/protocol   [aliases ...]   [# comment]" }
{ FS = "[<>]" }
(/<record/) { n=u=p=d=c=h="" }
(/<name/ && !/\(/) { n=$3 }
(/<number/) { u=$3 }
(/<protocol/) { p=$3 }
(/<description/) { d=$3 }
(/Unassigned/ || /Reserved/ || /historic/) { c=1 }
(/historic/) { h=1 }
(/<\/record/ && u && p && !h) { if(!n) c=1; if(c) n="#" n; else d="# " d; printf "%-16s %5i/%-6s %s\n", n,u,p,d }
