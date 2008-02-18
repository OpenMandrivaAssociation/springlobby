
%define name	springlobby
%define version	0.0.1.0735
%define rel	1

Summary:	Cross-platform lobby client for the Spring RTS project
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Group:		Games/Strategy
URL:		http://springlobby.info/
Source:		http://www.springlobby.info/tarballs/springlobby-%{version}.tar.bz2
Source1:	springlobby-logo.svg
# The warning is showed unconditionally, even if we use wx2.8:
Patch0:		springlobby-0.0.1.0735-drop-wx2.6-warning.patch
# Change default springdir from . to ~/.spring:
Patch1:		springlobby-0.0.1.0735-default-springdir.patch
# bundled springsettings is GPLv3+
License:	GPL+ and GPLv3+
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	wxgtku-devel
BuildRequires:	imagemagick
Requires:	spring

%description
SpringLobby is a free cross-platform lobby client for the Spring RTS
project.

This package also contains SpringSettings, a Spring configuration
tool.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_5x --bindir=%{_gamesbindir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -d -m755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%name.desktop <<EOF
[Desktop Entry]
Name=Spring Lobby
Comment=Play real-time strategy games using the Spring engine
Exec=%{_gamesbindir}/springlobby
Icon=springlobby
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF
cat > %{buildroot}%{_datadir}/applications/mandriva-springsettings.desktop <<EOF
[Desktop Entry]
Name=SpringSettings
Comment=Configure settings of Spring
Exec=%{_gamesbindir}/springsettings
Icon=springsettings
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

# TODO: put the svg itself into proper xdg dir
install -d -m755 %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
# (Anssi 01/2008) img not working properly with imagemagick svg support, corruption ensues
#convert %SOURCE1 -resize 48x48 %{buildroot}%{_liconsdir}/springlobby.png
#convert %SOURCE1 -resize 32x32 %{buildroot}%{_iconsdir}/springlobby.png
#convert %SOURCE1 -resize 16x16 %{buildroot}%{_miconsdir}/springlobby.png
convert src/images/springlobby.xpm -resize 48x48 %{buildroot}%{_liconsdir}/springlobby.png
convert src/images/springlobby.xpm -resize 32x32 %{buildroot}%{_iconsdir}/springlobby.png
convert src/images/springlobby.xpm -resize 16x16 %{buildroot}%{_miconsdir}/springlobby.png
convert src/images/springsettings.xpm -resize 48x48 %{buildroot}%{_liconsdir}/springsettings.png
convert src/images/springsettings.xpm -resize 32x32 %{buildroot}%{_iconsdir}/springsettings.png
convert src/images/springsettings.xpm -resize 16x16 %{buildroot}%{_miconsdir}/springsettings.png

%clean
rm -rf %{buildroot}

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%doc THANKS AUTHORS
%{_gamesbindir}/springlobby
%{_gamesbindir}/springsettings
%{_datadir}/applications/mandriva-springlobby.desktop
%{_datadir}/applications/mandriva-springsettings.desktop
%{_liconsdir}/spring*.png
%{_iconsdir}/spring*.png
%{_miconsdir}/spring*.png
