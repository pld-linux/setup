Summary:	Simple setup files
Summary(de):	Einfache Setup-Dateien 
Summary(fr):	Fichiers de configuration simples
Summary(pl):	Podstawowe pliki systemu Linux
Summary(tr):	Basit kurulum dosyalarý
Name:		setup
Version:	1.9.6
Release:	2
Copyright:	public domain
Group:		Base
Group(pl):	Podstawowe
Source:		%{name}-%{version}.tar.bz2
Patch0:		%{name}.patch
Buildroot:	/tmp/%{name}-%{version}-root
Buildarch:	noarch

%description
This package contains a number of very important configuration
and setup files, including the passwd, group, profile files, etc.

%description -l pl
Pakiet ten zawiera wiele bardzo wa¿nych plików konfiguracyjnych dla
twojego systemu.

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
%setup -q -n %{name}
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT

cp -a * $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%config(noreplace) %verify(not md5 size mtime) /etc/passwd
%config(noreplace) %verify(not md5 size mtime) /etc/group
%config(noreplace) %verify(not md5 size mtime) /etc/services
%config(noreplace) %verify(not md5 size mtime) /etc/host.conf
%config(noreplace) %verify(not md5 size mtime) /etc/motd
%config(noreplace) %verify(not md5 size mtime) /etc/printcap
%config(noreplace) %verify(not md5 size mtime) /etc/profile
%config(noreplace) %verify(not md5 size mtime) /etc/protocols

%attr(600,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/secure*

%changelog
* Fri May 28 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- ttyS0 >> /etc/securetty
- added group console gid=20 (removed from dev-*)
- group games changed gid -- now gid=21

* Wed May 19 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- removed qmail, zmailer, goopher & other users from group & /etc/passwd 
- removed icmp group & gid=80
  (wywaliæ ten wpis przed fina³owym budowaniem!)
- /lib/security >/dev/null
- /var/log >/dev/null
- standard Unix users like ftp/http/uucp/news/lp was save !

  it must be present on PLD Linux <amen> (no comments, no discuss allowed ;)

- home dir for adm was changed to /var/account,
- /etc/profile.d >/dev/null,
- group floppy again in /etc/group,
- ttyS1 >> /etc/securetty.

* Thu Apr 22 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.9.5-2]
- removed /etc/security and /etc/profile.d (now in filesystem)
- compiled on rpm 3

* Thu Feb 18 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.9.6-1d]
- /etc/shell -- back again ;)
- %dir /etc/security,
- %ghost /var/log/lastlog,
- %dir /lib/security.

* Fri Jan 22 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.9.5-1d]
- added new services,
- added Group(pl).

* Wed Jan 06 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [1.9.4-1d]
- added new services: fsp, ssh, ipx, https, cvspserver, mrt
- fixed petidomo uid & gid -- conflicts with qmail.

* Wed Dec 23 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [1.9.3-1d]
- added http and nofiles group
- added mailq, radius and radacct to services

* Sat Nov 07 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.9.2-2d]
- removed hosts.{allow,deny},
- minor changes.

* Mon Jun 29 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.9.2-1d]
- build against PLD,
- translation modified for pl,
- added some new IPv6 protocols,
- added /bin/false as a shell,
- added new group icmp (gid=55),
- start at RH spec file ..
