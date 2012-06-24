Summary:	Simple setup files
Summary(de):	Einfache Setup-Dateien
Summary(es):	Varios archivos b�sicos de configuraci�n
Summary(fr):	Fichiers de configuration simples
Summary(ja):	����ץ륻�åȥ��åץե�����
Summary(pl):	Podstawowe pliki systemu Linux
Summary(pt_BR):	V�rios arquivos b�sicos de configura��o
Summary(tr):	Basit kurulum dosyalar�
Name:		setup
Version:	2.4.3
Release:	0.1
License:	Public Domain
Group:		Base
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Buildarch:	noarch
AutoReqProv:	no

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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

cp -fa * $RPM_BUILD_ROOT

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

%dir /etc/profile.d
%attr(755,root,root) /etc/profile.d/*.sh
%attr(755,root,root) /etc/profile.d/*.csh
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/passwd
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/group
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/services
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/host.conf
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/hosts
%config(noreplace,missingok) %verify(not md5 size mtime) %{_sysconfdir}/motd
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/profile
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/protocols
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/fstab
%config(noreplace,missingok) %verify(not md5 size mtime) %{_sysconfdir}/filesystems
%config(noreplace,missingok) %verify(not md5 size mtime) %{_sysconfdir}/resolv.conf
%ghost %{_sysconfdir}/shells

%attr(600,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/secure*
