#
# TODO:
# - make some README.PLD with system features description
#
# Conditional build:
%bcond_with	ssp	# enable stack-smashing protector (vide dietlibc.spec)
#
%define	iana_etc_ver	1.04
%undefine	with_ccache
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
Version:	2.4.10
Release:	2.1
License:	Public Domain, partially BSD-like
Group:		Base
Source0:	ftp://distfiles.pld-linux.org/src/%{name}-%{version}.tar.bz2
# Source0-md5:	7f50f1650e961a77b18afa0a4a588fc1
Source1:	http://www.sethwklein.net/projects/iana-etc/downloads/iana-etc-%{iana_etc_ver}.tar.bz2
# Source1-md5:	9f769f7b2d0e519cf62dacb2b3b051d4
Source2:	%{name}-update-fstab.c
# This is source of non-iana changes in services file
#Patch0:		%{name}-services.patch
Patch0:		%{name}-securetty.patch
Patch1:		%{name}-profile.env.patch
BuildRequires:	dietlibc-static
BuildRequires:	gawk
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
%setup -q -a1
%patch0 -p1
%patch1 -p1
install %{SOURCE2} update-fstab.c

%build
%{__make} -C iana-etc-%{iana_etc_ver}

%{__make} \
	OPT_FLAGS="%{rpmcflags} %{?with_ssp:-fno-stack-protector}" \
	LDFLAGS="%{rpmldflags}" \
	CC="diet %{__cc}"
%{__make} update-fstab \
	OPT_FLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	CC="diet %{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/shrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install update-fstab $RPM_BUILD_ROOT%{_sbindir}

install iana-etc-%{iana_etc_ver}/protocols $RPM_BUILD_ROOT%{_sysconfdir}/protocols
# don't overwrite files from setup tar-ball, fix it in original tar!
#install iana-etc-%{iana_etc_ver}/services $RPM_BUILD_ROOT%{_sysconfdir}/services

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -p %{_sbindir}/joinpasswd -- %{name} < %{version}-%{release}

%triggerin -p %{_sbindir}/update-fstab -- %{name} < 2.4.10-1

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_sbindir}/joinpasswd
%attr(755,root,root) %{_sbindir}/update-fstab
%attr(755,root,root) /etc/profile.d/*.sh
%attr(755,root,root) /etc/profile.d/*.csh
%dir /etc/profile.d
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/env.d/*
%dir %{_sysconfdir}/env.d
%dir %{_sysconfdir}/shrc.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/fstab
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/group
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/host.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/hosts
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/passwd
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/profile
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/protocols
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/secure*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/services
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/filesystems
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/motd
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/resolv.conf
%ghost %{_sysconfdir}/shells
