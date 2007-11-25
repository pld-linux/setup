#
# TODO:
# - make some README.PLD with system features description
#
%define	iana_etc_ver	2.20
%undefine	with_ccache
#
Summary:	Simple setup files
Summary(de.UTF-8):	Einfache Setup-Dateien
Summary(es.UTF-8):	Varios archivos básicos de configuración
Summary(fr.UTF-8):	Fichiers de configuration simples
Summary(ja.UTF-8):	サンプルセットアップファイル
Summary(pl.UTF-8):	Podstawowe pliki systemu Linux
Summary(pt_BR.UTF-8):	Vários arquivos básicos de configuração
Summary(tr.UTF-8):	Basit kurulum dosyaları
Name:		setup
Version:	2.4.11
Release:	2
License:	Public Domain, partially BSD-like
Group:		Base
Source0:	ftp://distfiles.pld-linux.org/src/%{name}-%{version}.tar.bz2
# Source0-md5:	16589949b4c1b2ca3222a29e04f86f00
Source1:	http://sethwklein.net/projects/iana-etc/downloads/iana-etc-%{iana_etc_ver}.tar.bz2
# Source1-md5:	51d584b7b6115528c21e8ea32250f2b1
Source2:	%{name}-update-fstab.c
Source3:	postshell.c
Patch0:		%{name}-securetty.patch
Patch1:		%{name}-profile.env.patch
Patch2:		%{name}-iana-etc.patch
# This is source of non-iana changes in services file
Patch3:		%{name}-services.patch
BuildRequires:	dietlibc-static
BuildRequires:	gawk
Conflicts:	FHS < 2.3
Conflicts:	glibc < 6:2.4-4.1
AutoReqProv:	no
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This package contains a number of very important configuration and
setup files, including the passwd, group, profile files, etc.

%description -l de.UTF-8
Dieses Paket enthält wichtige Konfigurations- und Setup-Dateien, u.a.
passwd-, group-, profile-Dateien usw.

%description -l es.UTF-8
Este paquete contiene una variedad de archivos de configuración y
setup muy importantes, incluyendo el passwd, group, archivos de
"perfil", etc.

%description -l fr.UTF-8
Ce paquetage contient un nombre de fichiers de configuration très
importants, comme passwd, group, les fichiers profile, etc.

%description -l ja.UTF-8
このsetupパッケージには、passwd, group, profile などの、
重要なシステム設定ファイルが含まれてます。

%description -l pl.UTF-8
Pakiet ten zawiera wiele bardzo ważnych plików konfiguracyjnych dla
Twojego systemu.

%description -l pt_BR.UTF-8
Este pacote contém uma variedade de arquivos de configuração e setup
muito importantes, incluindo o passwd, group, arquivos de "perfil",
etc.

%description -l tr.UTF-8
Bu paket, passwd, group, profile gibi çok önemli ayar ve kurulum
dosyalarını içerir.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
install %{SOURCE2} update-fstab.c
install %{SOURCE3} postshell.c

%build
%{__make} -C iana-etc-%{iana_etc_ver}
%{__patch} iana-etc-%{iana_etc_ver}/services %{PATCH3}

%{__make} \
	OPT_FLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmcflags} %{rpmldflags}" \
	CC="diet %{__cc}"
%{__make} postshell update-fstab \
	OPT_FLAGS="%{rpmcflags} -Os" \
	LDFLAGS="%{rpmcflags} %{rpmldflags}" \
	CC="diet %{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/shrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install postshell $RPM_BUILD_ROOT%{_sbindir}
install update-fstab $RPM_BUILD_ROOT%{_sbindir}

install iana-etc-%{iana_etc_ver}/protocols $RPM_BUILD_ROOT%{_sysconfdir}/protocols
# don't overwrite files from setup tarball, apply changes to setup module instead
%if "%{version}" == "2.4.11"
# 2.4.12 will contain iana-etc update
install iana-etc-%{iana_etc_ver}/services $RPM_BUILD_ROOT%{_sysconfdir}/services
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -p %{_sbindir}/joinpasswd -- %{name} < %{version}-%{release}

%triggerin -p %{_sbindir}/update-fstab -- %{name} < 2.4.10-1

%post -p /sbin/postshell
-/sbin/env-update -u

%postun -p /sbin/postshell
-/sbin/env-update -u

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_sbindir}/joinpasswd
%attr(755,root,root) %{_sbindir}/postshell
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
