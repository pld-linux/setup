#
# TODO:
# - make some README.PLD with system features description
#
# Conditional build:
%bcond_with	ssp	# disable stack-smashing protector (vide dietlibc.spec)
#
Summary:	Simple setup files
Summary(de):	Einfache Setup-Dateien
Summary(es):	Varios archivos básicos de configuración
Summary(fr):	Fichiers de configuration simples
Summary(ja):	¥µ¥ó¥×¥ë¥»¥Ã¥È¥¢¥Ã¥×¥Õ¥¡¥¤¥ë
Summary(pl):	Podstawowe pliki systemu Linux
Summary(pt_BR):	Vários arquivos básicos de configuração
Summary(tr):	Basit kurulum dosyalarý
Name:		setup
Version:	2.4.6
Release:	2
License:	Public Domain, partially BSD-like
Group:		Base
Source0:	http://piorun.ds.pg.gda.pl/~blues/SOURCES/%{name}-%{version}.tar.bz2
# Source0-md5:	33afa2766c28f1fb8331bd9209bf6b04
Patch0:		setup-fstab.patch
BuildRequires:	dietlibc-static
Conflicts:	FHS < 2.3
AutoReqProv:	no
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This package contains a number of very important configuration and
setup files, including the passwd, group, profile files, etc.

%description -l de
Dieses Paket enthält wichtige Konfigurations- und Setup-Dateien, u.a.
passwd-, group-, profile-Dateien usw.

%description -l es
Este paquete contiene una variedad de archivos de configuración y
setup muy importantes, incluyendo el passwd, group, archivos de
"perfil", etc.

%description -l fr
Ce paquetage contient un nombre de fichiers de configuration très
importants, comme passwd, group, les fichiers profile, etc.

%description -l ja
¤³¤Îsetup¥Ñ¥Ã¥±¡¼¥¸¤Ë¤Ï¡¢passwd, group, profile ¤Ê¤É¤Î¡¢
½ÅÍ×¤Ê¥·¥¹¥Æ¥àÀßÄê¥Õ¥¡¥¤¥ë¤¬´Þ¤Þ¤ì¤Æ¤Þ¤¹¡£

%description -l pl
Pakiet ten zawiera wiele bardzo wa¿nych plików konfiguracyjnych dla
Twojego systemu.

%description -l pt_BR
Este pacote contém uma variedade de arquivos de configuração e setup
muito importantes, incluindo o passwd, group, arquivos de "perfil",
etc.

%description -l tr
Bu paket, passwd, group, profile gibi çok önemli ayar ve kurulum
dosyalarýný içerir.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	OPT_FLAGS="%{rpmcflags} %{?with_pp:-fno-stack-protector}" \
	CC="diet %{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/shrc.d

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -p %{_sbindir}/joinpasswd -- %{name} < %{version}-%{release}

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_sbindir}/joinpasswd
%attr(755,root,root) /etc/profile.d/*.sh
%attr(755,root,root) /etc/profile.d/*.csh
%dir /etc/profile.d
%attr(644,root,root) %config(noreplace,missingok) %verify(not md5 size mtime) /etc/env.d/*
%dir /etc/env.d
%dir /etc/shrc.d
%attr(644,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/fstab
%attr(644,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/group
%attr(644,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/host.conf
%attr(644,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/hosts
%attr(644,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/passwd
%attr(644,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/profile
%attr(644,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/protocols
%attr(600,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/secure*
%attr(644,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/services
%attr(644,root,root) %config(noreplace,missingok) %verify(not md5 size mtime) %{_sysconfdir}/filesystems
%attr(644,root,root) %config(noreplace,missingok) %verify(not md5 size mtime) %{_sysconfdir}/motd
%attr(644,root,root) %config(noreplace,missingok) %verify(not md5 size mtime) %{_sysconfdir}/resolv.conf
%ghost %{_sysconfdir}/shells
