Summary:	Simple setup files
Summary(de):	Einfache Setup-Dateien 
Summary(fr):	Fichiers de configuration simples
Summary(pl):	Podstawowe pliki systemu Linux
Summary(tr):	Basit kurulum dosyalar�
Name:		setup
Version:	1.9.5
Release:	2
Copyright:	public domain
Group:		Base
Group(pl):	Bazowe
Source:		%{name}-%{version}.tar.bz2
Buildroot:	/tmp/%{name}-%{version}-root
Buildarch:	noarch

%description
This package contains a number of very important configuration
and setup files, including the passwd, group, profile files, etc.

%description -l pl
Pakiet ten zawiera wiele bardzo wa�nych plik�w konfiguracyjnych dla
twojego systemu.

%description -l de
Dieses Paket enth�lt wichtige Konfigurations- und Setup-Dateien,
u.a. passwd-, group-, profile-Dateien usw.

%description -l fr
Ce paquetage contient un nombre de fichiers de configuration tr�s
importants, comme passwd, group, les fichiers profile, etc.

%description -l tr
Bu paket, passwd, group, profile gibi �ok �nemli ayar ve kurulum dosyalar�n�
i�erir.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/var/log
install -d $RPM_BUILD_ROOT/lib/security

cp -a * $RPM_BUILD_ROOT
touch $RPM_BUILD_ROOT/var/log/lastlog

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

%ghost /var/log/lastlog

%changelog
* Wed May 19 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
- removed qmail, zmailer, goopher, news & other users from group & /etc/passwd 
- removed icmp group & gid=80
  (wywali� ten wpis przed fina�owym budowaniem!)

* Thu Apr 22 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.9.5-2]
- removed /etc/security and /etc/profile.d (now in filesystem)
- compiled on rpm 3

* Thu Feb 18 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.9.6-1d]
- /etc/shell -- back again ;)
- %dir /etc/security,
- %ghost /var/log/lastlog,
- %dir /lib/security.

* Fri Jan 22 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.9.5-1d]
- added new services,
- added Group(pl).

* Wed Jan 06 1999 Arkadiusz Mi�kiewicz <misiek@misiek.eu.org>
  [1.9.4-1d]
- added new services: fsp, ssh, ipx, https, cvspserver, mrt
- fixed petidomo uid & gid -- conflicts with qmail.

* Wed Dec 23 1998 Arkadiusz Mi�kiewicz <misiek@misiek.eu.org>
  [1.9.3-1d]
- added http and nofiles group
- added mailq, radius and radacct to services

* Sat Nov 07 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.9.2-2d]
- removed hosts.{allow,deny},
- minor changes.

* Mon Jun 29 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.9.2-1d]
- build against PLD,
- translation modified for pl,
- added some new IPv6 protocols,
- added /bin/false as a shell,
- added new group icmp (gid=55),
- start at RH spec file ..
