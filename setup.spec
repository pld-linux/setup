Summary:	Simple setup files
Summary(de):	Einfache Setup-Dateien 
Summary(fr):	Fichiers de configuration simples
Summary(pl):	Podstawowe pliki systemu Linux
Summary(tr):	Basit kurulum dosyalarý
Name:		setup
Version:	2.3.2
Release:	1
License:	public domain
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Buildarch:	noarch
AutoReqProv:	no

%description
This package contains a number of very important configuration and
setup files, including the passwd, group, profile files, etc.

%description -l pl
Pakiet ten zawiera wiele bardzo wa¿nych plików konfiguracyjnych dla
twojego systemu.

%description -l de
Dieses Paket enthält wichtige Konfigurations- und Setup-Dateien, u.a.
passwd-, group-, profile-Dateien usw.

%description -l fr
Ce paquetage contient un nombre de fichiers de configuration très
importants, comme passwd, group, les fichiers profile, etc.

%description -l tr
Bu paket, passwd, group, profile gibi çok önemli ayar ve kurulum
dosyalarýný içerir.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT

cp -a * $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

#%triggerin -- %{name} < %{version}-%{release}
#[ "$1" = "1" ] && exit 0
#[ ! -e /etc/group.rpmnew ] && exit 0
#cat /etc/group.rpmnew | while read GROUPLINE ; do
#	GR="`echo $GROUPLINE | cut -f 1 -d ':'`"
#	if ! grep -q "^$GR" /etc/group ; then
#		echo "$GROUPLINE" >> /etc/group
#	fi
#done

%files
%defattr(644,root,root,755)

%dir %{_sysconfdir}/profile.d
%attr(755,root,root) %{_sysconfdir}/profile.d/*.sh
%attr(755,root,root) %{_sysconfdir}/profile.d/*.csh
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/passwd
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/group
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/services
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/host.conf
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/hosts
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/motd
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/profile
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/protocols
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/filesystems
%ghost %{_sysconfdir}/shells

%attr(600,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/secure*
