Summary:	Simple setup files
Summary(de):	Einfache Setup-Dateien 
Summary(fr):	Fichiers de configuration simples
Summary(pl):	Podstawowe pliki systemu Linux
Summary(tr):	Basit kurulum dosyalar�
Name:		setup
Version:	1.9.6
Release:	2
Copyright:	public domain
Group:		Base
Group(pl):	Podstawowe
Source:		%{name}-%{version}.tar.bz2
Patch0:		%{name}.patch
Patch1:		%{name}-rootshell.patch
Patch2:		%{name}-icmp6.patch
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
%setup  -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT

cp -a * $RPM_BUILD_ROOT

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
