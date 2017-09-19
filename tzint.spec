%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          tzint
Summary:       tcl package for libzint barcode encoding library
Version:       1.0
Release:       0
License:       BSD 3-Clause License
Group:         Development/Libraries/Tcl
Source:        tzint1.0-src.tar.gz
URL:           https://sourceforge.net/projects/tclsnippets/files/tzint/
BuildRequires: autoconf
BuildRequires: make
BuildRequires: libpng16-compat-devel
BuildRequires: tcl-devel >= 8.6
BuildRequires: zlib-devel
Requires:      tcl >= 8.6
BuildRoot:     %{buildroot}

%description
A barcode encoding library supporting over 50 symbologies including
Code 128, Data Matrix, USPS OneCode, EAN-128, UPC/EAN, ITF, QR Code,
Code 16k, PDF417, MicroPDF417, LOGMARS, Maxicode, GS1 DataBar, Aztec,
Composite Symbols and more.

%prep
%setup -q -n %{name}%{version}

%build
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib} \
%ifarch x86_64
	--enable-64bit=yes \
%endif
	--with-tcl=%{directory}/%{_lib}
make 

%install
make DESTDIR=%{buildroot} pkglibdir=%{directory}/%{_lib}/tcl/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%doc LICENSE.zint license.terms
%defattr(-,root,root)
%{directory}/%{_lib}/tcl
/usr/share/man/mann

