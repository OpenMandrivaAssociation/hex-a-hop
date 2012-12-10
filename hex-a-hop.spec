Name:		hex-a-hop
Version:	1.1.0
Release:	%mkrel 1
Summary:	A hexagonal tile-based puzzle game
Group:		Games/Puzzles
License:	GPL
URL:		http://hexahop.sourceforge.net/
Source:		http://sourceforge.net/projects/hexahop/files/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	imagemagick

%description
Hex-a-Hop is a hexagonal tile-based puzzle game with one simple goal:
destroy all green tiles! There are infinite undos and no time limits --
you just have to find a way to destroy all the green tiles and step on
a safe tile at the end.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

# icons
for N in 16 32 48 64 128; do convert data/icon.bmp -resize ${N}x${N} $N.png; done
%__install -D 16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%__install -D 32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%__install -D 48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%__install -D 64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%__install -D 128.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# XDG menu entry
%__mkdir_p  %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=Hex-a-hop
Comment=Hexagonal tile-based puzzle
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=Game;LogicGame;
EOF

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png



%changelog
* Wed Mar 28 2012 Andrey Bondrov <abondrov@mandriva.org> 1.1.0-1
+ Revision: 787934
- imported package hex-a-hop

