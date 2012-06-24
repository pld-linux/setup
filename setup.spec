# TODO:
# - make some README.PLD with system features description
# - use joinpasswd in post
Summary:	Simple setup files
Summary(de):	Einfache Setup-Dateien
Summary(es):	Varios archivos b�sicos de configuraci�n
Summary(fr):	Fichiers de configuration simples
Summary(ja):	����ץ륻�åȥ��åץե�����
Summary(pl):	Podstawowe pliki systemu Linux
Summary(pt_BR):	V�rios arquivos b�sicos de configura��o
Summary(tr):	Basit kurulum dosyalar�
Name:		setup
Version:	2.4.4
Release:	1
License:	Public Domain, partially BSD-like
Group:		Base
Source0:	http://piorun.ds.pg.gda.pl/~blues/SOURCES/%{name}-%{version}.tar.bz2
# Source0-md5:	74484812aa2e01e5b2fa5c4e8276969a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
AutoReqProv:	no

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
%setup -q 

%build
%{__make} \
	OPT_FLAGS="%{rpmcflags}" \
	CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc ChangeLog
%attr(755,root,root) %{_sbindir}/joinpasswd
%attr(755,root,root) /etc/profile.d/*.sh
%attr(755,root,root) /etc/profile.d/*.csh
%dir /etc/profile.d
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
