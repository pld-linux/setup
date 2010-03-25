#
# TODO:
# - make some README.PLD with system features description
#
%define	iana_etc_ver	2.30
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
Version:	2.7.2
Release:	1
License:	Public Domain, partially BSD-like
Group:		Base
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	e82bfb86a430f2f08ecc48971f60dcc5
# http://sethwklein.net/iana-etc
Source1:	http://sethwklein.net/projects/iana-etc/downloads/iana-etc-%{iana_etc_ver}.tar.bz2
# Source1-md5:	3ba3afb1d1b261383d247f46cb135ee8
Source2:	http://www.iana.org/assignments/protocol-numbers/index.txt
# Source2-md5:	33440b7d913303a6051ae64290f0ab21
Source3:	http://www.iana.org/assignments/port-numbers
# Source3-md5:	8e19a2c7cf60baabf919de1cc89a1cbb
Patch0:		%{name}-iana-etc.patch
# This is source of non-iana changes in services file
Patch1:		%{name}-services.patch
Patch2:		protocols-fmt.patch
BuildRequires:	dietlibc-static
BuildRequires:	gawk
Requires:	FHS >= 2.3-24.1
Provides:	group(fuse)
Conflicts:	PowerChutePlus < 4.5.3-2
Conflicts:	glibc < 6:2.4-4.1
# tape,dialout and cdrom groups support
Conflicts:	dev < 3.4-4
Conflicts:	udev < 1:138-5
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
mv iana-etc{-%{iana_etc_ver},}
%patch2 -p1

cp -a %{SOURCE2} iana-etc/protocol-numbers.iana
cp -a %{SOURCE3} iana-etc/port-numbers.iana

%build
%{__make} -C iana-etc
%{__patch} iana-etc/services %{PATCH1}

# kill trailing spaces/tabs
%{__sed} -i -e 's,[ \t]\+$,,' iana-etc/{services,protocols}

%{__make} \
	CC="diet %{__cc}" \
	OPT_FLAGS="%{rpmcflags} -Os" \
	LDFLAGS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/shrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a iana-etc/{services,protocols} $RPM_BUILD_ROOT%{_sysconfdir}

# not packaged
rm $RPM_BUILD_ROOT%{_sysconfdir}/{mtab,netgroup,suid_profile}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -p /sbin/postshell -- %{name} < %{version}-%{release}
%{_sbindir}/joinpasswd
%{_sbindir}/delpasswd -g ttyS cdwrite

%triggerin -p %{_sbindir}/update-fstab -- %{name} < 2.4.10-1

%post -p /sbin/postshell
-/sbin/env-update -u

%postun -p /sbin/postshell
-/sbin/env-update -u

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_sbindir}/delpasswd
%attr(755,root,root) %{_sbindir}/joinpasswd
%attr(755,root,root) %{_sbindir}/postshell
%attr(755,root,root) %{_sbindir}/update-fstab
%config(noreplace,missingok) %verify(not md5 mtime size) %attr(755,root,root) /etc/profile.d/*.sh
%config(noreplace,missingok) %verify(not md5 mtime size) %attr(755,root,root) /etc/profile.d/*.csh
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
