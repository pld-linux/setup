Summary:     Simple setup files
Summary(de): Einfache Setup-Dateien 
Summary(fr): Fichiers de configuration simples
Summary(tr): Basit kurulum dosyalarý
Name:        setup
Version:     1.10.0
Release:     3
Copyright:   public domain
Source:      %{name}-%{version}.tar.bz2
Group:       Base
Buildroot:   /tmp/%{name}-%{version}-root
BuildArchitectures: noarch

%description
This package contains a number of very important configuration
and setup files, including the passwd, group, profile files, etc.

%description -l de
Dieses Paket enthält wichtige Konfigurations- und Setup-Dateien,
u.a. passwd-, group-, profile-Dateien usw.

%description -l fr
Ce paquetage contient un nombre de fichiers de configuration très
importants, comme passwd, group, les fichiers profile, etc.

%description -l tr
Bu paket, passwd, group, profile gibi çok önemli ayar ve kurulum dosyalarýný
içerir.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/profile.d,var/log}

cp -R * $RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT/var/log/lastlog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%verify(not md5 size mtime) %config(noreplace) /etc/passwd
%verify(not md5 size mtime) %config(noreplace) /etc/group
%config /etc/services
%config /etc/host.conf
%config /etc/motd
%config /etc/printcap
%config /etc/profile
%config /etc/protocols
%attr(600, root, root) %config(missingok) /etc/securetty
%attr(600, root, root) %verify(not md5 size mtime) %config(noreplace) /etc/shadow
%config /etc/csh.cshrc
%dir /etc/profile.d
%verify(not md5 size mtime) /var/log/lastlog

%changelog
* Sun Oct  4 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.10.0-3]
- added radius and radacct in /etc/services.

* Wed Sep 30 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.10.0-2]
- added zmailer group in /etc/group.

* Thu Sep  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.10.0-1]
- /etc/hosts.{allow,deny} moved tcp_wrappers,
- /etc/exports moved to nfs-server,
- added qmail and http users and groups,
- added "mailq  174/tcp" in /etc/services for Zmailer,
- added /etc/shadow.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Dec 05 1997 Erik Troan <ewt@redhat.com>
- /etc/profile uses $i, which needs to be unset

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- made /etc/passwd and /etc/group %config(noreplace)

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- removed /etc/inetd.conf, /etc/rpc
- flagged /etc/securetty as missingok
- fixed buildroot stuff in spec file

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Wed Apr 16 1997 Erik Troan <ewt@redhat.com>
- Don't verify md5sum, size, or timestamp of /var/log/lastlog, /etc/passwd,
  or /etc/group.
