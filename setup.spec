#
# TODO:
# - make some README.PLD with system features description
#
# Conditional build:
%bcond_with	ssp	# disable stack-smashing protector (vide dietlibc.spec)
#
%define	iana_etc_ver	1.03
#
Summary:	Simple setup files
Summary(de):	Einfache Setup-Dateien
Summary(es):	Varios archivos b�sicos de configuraci�n
Summary(fr):	Fichiers de configuration simples
Summary(ja):	����ץ륻�åȥ��åץե�����
Summary(pl):	Podstawowe pliki systemu Linux
Summary(pt_BR):	V�rios arquivos b�sicos de configura��o
Summary(tr):	Basit kurulum dosyalar�
Name:		setup
Version:	2.4.6
Release:	8.2
License:	Public Domain, partially BSD-like
Group:		Base
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	33afa2766c28f1fb8331bd9209bf6b04
Source1:	http://www.sethwklein.net/projects/iana-etc/downloads/iana-etc-%{iana_etc_ver}.tar.bz2
# Source1-md5:	670da9e41179d618498f5d614b7f4636
Patch0:		%{name}-fstab.patch
Patch1:		%{name}-special_users.patch
BuildRequires:	dietlibc-static
BuildRequires:	gawk
Conflicts:	FHS < 2.3
AutoReqProv:	no
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch alpha
Obsoletes:	gfax
%endif

%define		_sbindir	/sbin

%description
This package contains a number of very important configuration and
setup files, including the passwd, group, profile files, etc.

%description -l de
Dieses Paket enth�lt wichtige Konfigurations- und Setup-Dateien, u.a.
passwd-, group-, profile-Dateien usw.

%description -l es
Este paquete contiene una variedad de archivos de configuraci�n y
setup muy importantes, incluyendo el passwd, group, archivos de
"perfil", etc.

%description -l fr
Ce paquetage contient un nombre de fichiers de configuration tr�s
importants, comme passwd, group, les fichiers profile, etc.

%description -l ja
����setup�ѥå������ˤϡ�passwd, group, profile �ʤɤΡ�
���פʥ����ƥ�����ե����뤬�ޤޤ�Ƥޤ���

%description -l pl
Pakiet ten zawiera wiele bardzo wa�nych plik�w konfiguracyjnych dla
Twojego systemu.

%description -l pt_BR
Este pacote cont�m uma variedade de arquivos de configura��o e setup
muito importantes, incluindo o passwd, group, arquivos de "perfil",
etc.

%description -l tr
Bu paket, passwd, group, profile gibi �ok �nemli ayar ve kurulum
dosyalar�n� i�erir.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1

%build
%{__make} -C iana-etc-%{iana_etc_ver}

%{__make} \
	OPT_FLAGS="%{rpmcflags} %{?with_ssp:-fno-stack-protector}" \
	CC="diet %{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/shrc.d

install iana-etc-%{iana_etc_ver}/protocols $RPM_BUILD_ROOT/etc/protocols
install iana-etc-%{iana_etc_ver}/services $RPM_BUILD_ROOT/etc/services

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
%attr(644,root,root) %config(noreplace,missingok) %verify(not md5 size mtime) %{_sysconfdir}/env.d/*
%dir %{_sysconfdir}/env.d
%dir %{_sysconfdir}/shrc.d
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
