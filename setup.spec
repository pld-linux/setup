#
# TODO:
# - make some README.PLD with system features description
#
%bcond_without	diet

%define	iana_etc_ver	2.30
Summary:	Simple setup files
Summary(de.UTF-8):	Einfache Setup-Dateien
Summary(es.UTF-8):	Varios archivos básicos de configuración
Summary(fr.UTF-8):	Fichiers de configuration simples
Summary(ja.UTF-8):	サンプルセットアップファイル
Summary(pl.UTF-8):	Podstawowe pliki systemu Linux
Summary(pt_BR.UTF-8):	Vários arquivos básicos de configuração
Summary(tr.UTF-8):	Basit kurulum dosyaları
Name:		setup
Version:	2.9.0
Release:	1
License:	Public Domain, partially BSD-like
Group:		Base
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	2b5c3c03a77f8963ee1c4c269f0edfed
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
%if %{with diet}
BuildRequires:	dietlibc-static
%else
BuildRequires:	glibc-static
%endif
BuildRequires:	gawk
BuildRequires:	glibc-misc
Requires:	FHS >= 2.3-24.1
Provides:	group(fuse)
Conflicts:	PowerChutePlus < 4.5.3-2
Conflicts:	glibc < 6:2.4-4.1
# tape,dialout and cdrom groups support
Conflicts:	dev < 3.4-4
Conflicts:	udev < 1:138-5
# /etc/mtab being symlink to /proc/self/mounts
Conflicts:	rc-scripts < 0.4.5.1-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin
%undefine	with_ccache

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
	CC="%{?with_diet:diet }%{__cc}" \
	OPT_FLAGS="%{rpmcflags} -Os -D_LARGEFILE_SOURCE=1 -D_FILE_OFFSET_BITS=64" \
	LDFLAGS="%{rpmcflags} %{rpmldflags} -static"

ldd postshell | grep "not a dynamic executable" || exit 1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/shrc.d
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a iana-etc/{services,protocols} $RPM_BUILD_ROOT%{_sysconfdir}

# not packaged
%{__rm} $RPM_BUILD_ROOT%{_sysconfdir}/{netgroup,suid_profile}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerprein -p /sbin/postshell -- %{name} < %{version}-%{release}
-/bin/sh -c '/usr/bin/test -L /etc/mtab || /bin/mv -v /etc/mtab /etc/mtab.rpmsave'

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
%dir /etc/profile.d
%config(noreplace,missingok) %verify(not md5 mtime size) %attr(755,root,root) /etc/profile.d/tmp-dir.sh
%config(noreplace,missingok) %verify(not md5 mtime size) %attr(755,root,root) /etc/profile.d/tmp-dir.csh
%dir %{_sysconfdir}/env.d
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/env.d/EDITOR
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/env.d/HISTFILESIZE
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/env.d/HOME_ETC
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/env.d/MAILCHECK
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/env.d/MAILPATH
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/env.d/NNTPSERVER
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/env.d/ORGANIZATION
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/env.d/TMOUT
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/env.d/VISUAL
%dir %{_sysconfdir}/shrc.d
%config(noreplace) %verify(not md5 mtime size) /etc/shrc.d/256term.sh
%config(noreplace) %verify(not md5 mtime size) /etc/shrc.d/256term.csh
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/fstab
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/group
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/host.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/hosts
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/passwd
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/profile
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/protocols
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/securetty
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/services
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/filesystems
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/motd
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/resolv.conf
%ghost %{_sysconfdir}/shells
# symlink to /proc/self/mounts
%{_sysconfdir}/mtab
