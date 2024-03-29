#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : swayidle
Version  : 1.8.0
Release  : 7
URL      : https://github.com/swaywm/swayidle/archive/1.8.0/swayidle-1.8.0.tar.gz
Source0  : https://github.com/swaywm/swayidle/archive/1.8.0/swayidle-1.8.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: swayidle-bin = %{version}-%{release}
Requires: swayidle-data = %{version}-%{release}
Requires: swayidle-license = %{version}-%{release}
Requires: swayidle-man = %{version}-%{release}
BuildRequires : bash-completion-dev
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(fish)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : scdoc

%description
# swayidle
This is sway's idle management daemon, swayidle. It is compatible with any
Wayland compositor which implements the
[ext-idle-notify](https://gitlab.freedesktop.org/wayland/wayland-protocols/-/tree/main/staging/ext-idle-notify)
protocol or the KDE
[idle](https://github.com/swaywm/sway/blob/master/protocols/idle.xml) protocol.
See the man page, [swayidle(1)](./swayidle.1.scd), for instructions on configuring swayidle.

%package bin
Summary: bin components for the swayidle package.
Group: Binaries
Requires: swayidle-data = %{version}-%{release}
Requires: swayidle-license = %{version}-%{release}

%description bin
bin components for the swayidle package.


%package data
Summary: data components for the swayidle package.
Group: Data

%description data
data components for the swayidle package.


%package license
Summary: license components for the swayidle package.
Group: Default

%description license
license components for the swayidle package.


%package man
Summary: man components for the swayidle package.
Group: Default

%description man
man components for the swayidle package.


%prep
%setup -q -n swayidle-1.8.0
cd %{_builddir}/swayidle-1.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670508841
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/swayidle
cp %{_builddir}/swayidle-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/swayidle/701a0d07ac28d9dadb4826db3bf2176efc7316c4 || :
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/swayidle

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/swayidle
/usr/share/fish/vendor_completions.d/swayidle.fish
/usr/share/zsh/site-functions/_swayidle

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/swayidle/701a0d07ac28d9dadb4826db3bf2176efc7316c4

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/swayidle.1
