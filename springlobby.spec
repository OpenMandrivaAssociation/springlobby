%define Werror_cflags %nil

Summary:	Cross-platform lobby client for the Spring RTS project
Name:		springlobby
Version:	0.147
Release:	3
Group:		Games/Strategy
# bundled springsettings is GPLv3+
License:	GPL+ and GPLv3+
URL:		http://springlobby.info/
Source:		http://www.springlobby.info/tarballs/springlobby-%{version}.tar.bz2
Source1:	springlobby-logo.svg
Patch0:		springlobby-lpthread.patch
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	boost-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_sound-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	wxgtku2.8-devel
BuildRequires:	pkgconfig(libtorrent-rasterbar)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(libmpg123)
Requires:	spring
Requires:	curl
Requires:	openal

%description
SpringLobby is a free cross-platform lobby client for the Spring RTS
project.

This package also contains SpringSettings, a Spring configuration
tool.

%prep
%setup -q
%patch0 -p0 -b .lpthread
sed -i -e 's,springlobby.svg,springlobby,g' src/springlobby.desktop

%build
%cmake
%make

%install
%makeinstall_std -C build

desktop-file-install \
  --vendor="" \
  --remove-category="Application" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

install -d -m755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-springsettings.desktop <<EOF
[Desktop Entry]
Name=SpringSettings
Comment=Configure settings of Spring
Exec=springsettings
Icon=springsettings
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

install -d -m755 %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48,scalable}/apps
install -m644 src/images/springlobby.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/springlobby.svg
convert src/images/springlobby.svg -resize 48x48 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/springlobby.png
convert src/images/springlobby.svg -resize 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/springlobby.png
convert src/images/springlobby.svg -resize 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/springlobby.png
convert src/images/springsettings.xpm -resize 48x48 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/springsettings.png
convert src/images/springsettings.xpm -resize 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/springsettings.png
convert src/images/springsettings.xpm -resize 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/springsettings.png

%find_lang %{name}

%files -f %{name}.lang
%doc THANKS AUTHORS
%{_bindir}/springlobby
%{_bindir}/springsettings
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/mandriva-springsettings.desktop
%{_iconsdir}/hicolor/*/apps/*.*

