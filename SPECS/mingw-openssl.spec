%?mingw_package_header

# For the curious:
# 0.9.5a soversion = 0
# 0.9.6  soversion = 1
# 0.9.6a soversion = 2
# 0.9.6c soversion = 3
# 0.9.7a soversion = 4
# 0.9.7ef soversion = 5
# 0.9.8ab soversion = 6
# 0.9.8g soversion = 7
# 0.9.8jk + EAP-FAST soversion = 8
# 1.0.0 soversion = 10
%global soversion 10

# Enable the tests.
# These only work some of the time, but fail randomly at other times
# (although I have had them complete a few times, so I don't think
# there is any actual problem with the binaries).
%global run_tests 0

# Number of threads to spawn when testing some threading fixes.
%global thread_test_threads %{?threads:%{threads}}%{!?threads:1}

Name:           mingw-openssl
Version:        1.0.2k
Release:        2%{?dist}
Summary:        MinGW port of the OpenSSL toolkit

License:        OpenSSL
Group:          Development/Libraries
URL:            http://www.openssl.org/

# We have to remove certain patented algorithms from the openssl source
# tarball with the hobble-openssl script which is included below.
# The original openssl upstream tarball cannot be shipped in the .src.rpm.
Source:         openssl-%{version}-hobbled.tar.xz

Source1:        hobble-openssl
Source2:        Makefile.certificate
Source6:        make-dummy-cert
Source7:        renew-dummy-cert
Source8:        openssl-thread-test.c
Source9:        opensslconf-new.h
Source10:       opensslconf-new-warning.h
Source11:       README.FIPS
Source12:       ec_curve.c
Source13:       ectest.c

# Build changes
Patch1:         openssl-1.0.2e-rpmbuild.patch
Patch2:         openssl-1.0.2a-defaults.patch
Patch4:         openssl-1.0.2i-enginesdir.patch
Patch5:         openssl-1.0.2a-no-rpath.patch
Patch6:         openssl-1.0.2a-test-use-localhost.patch
Patch7:         openssl-1.0.0-timezone.patch
Patch8:         openssl-1.0.1c-perlfind.patch
Patch9:         openssl-1.0.1c-aliasing.patch
# Bug fixes
Patch23:        openssl-1.0.2c-default-paths.patch
Patch24:        openssl-1.0.2a-issuer-hash.patch
# Functionality changes
Patch33:        openssl-1.0.0-beta4-ca-dir.patch
Patch34:        openssl-1.0.2a-x509.patch
Patch35:        openssl-1.0.2a-version-add-engines.patch
# Patch39:        openssl-1.0.2a-ipv6-apps.patch
Patch40:        openssl-1.0.2i-fips.patch
Patch43:        openssl-1.0.2j-krb5keytab.patch
Patch45:        openssl-1.0.2a-env-zlib.patch
Patch47:        openssl-1.0.2a-readme-warning.patch
Patch49:        openssl-1.0.1i-algo-doc.patch
Patch50:        openssl-1.0.2a-dtls1-abi.patch
# Patch51:        openssl-1.0.2a-version.patch
# Patch56:        openssl-1.0.2a-rsa-x931.patch
Patch58:        openssl-1.0.2a-fips-md5-allow.patch
Patch60:        openssl-1.0.2a-apps-dgst.patch
# Patch63:        openssl-1.0.2k-starttls.patch
Patch65:        openssl-1.0.2i-chil-fixes.patch
Patch66:        openssl-1.0.2h-pkgconfig.patch
# Patch68:        openssl-1.0.2i-secure-getenv.patch
# Patch70:        openssl-1.0.2a-fips-ec.patch
Patch71:        openssl-1.0.2g-manfix.patch
# Patch72:        openssl-1.0.2a-fips-ctor.patch
Patch73:        openssl-1.0.2c-ecc-suiteb.patch
Patch74:        openssl-1.0.2j-deprecate-algos.patch
Patch75:        openssl-1.0.2a-compat-symbols.patch
# Patch76:        openssl-1.0.2j-new-fips-reqs.patch
Patch77:        openssl-1.0.2j-downgrade-strength.patch
Patch78:        openssl-1.0.2k-cc-reqs.patch
Patch90:        openssl-1.0.2i-enc-fail.patch
Patch94:        openssl-1.0.2d-secp256k1.patch
Patch95:        openssl-1.0.2e-remove-nistp224.patch
Patch96:        openssl-1.0.2e-speed-doc.patch
Patch97:        openssl-1.0.2k-no-ssl2.patch
Patch98:        openssl-1.0.2k-long-hello.patch
# Patch99:        openssl-1.0.2k-fips-randlock.patch
# Backported fixes including security fixes
Patch80:        openssl-1.0.2e-wrap-pad.patch
Patch81:        openssl-1.0.2a-padlock64.patch
Patch82:        openssl-1.0.2i-trusted-first-doc.patch
Patch83:        openssl-1.0.2k-backports.patch
Patch84:        openssl-1.0.2k-ppc-update.patch
Patch85:        openssl-1.0.2k-req-x509.patch
Patch86:        openssl-1.0.2k-cve-2017-3736.patch
Patch87:        openssl-1.0.2k-cve-2017-3737.patch
Patch88:        openssl-1.0.2k-cve-2017-3738.patch
Patch89:        openssl-1.0.2k-s390x-update.patch
Patch100:       openssl-1.0.2k-name-sensitive.patch
Patch101:       openssl-1.0.2k-cve-2017-3735.patch
Patch102:       openssl-1.0.2k-cve-2018-0732.patch
Patch103:       openssl-1.0.2k-cve-2018-0737.patch
Patch104:       openssl-1.0.2k-cve-2018-0739.patch
Patch105:       openssl-1.0.2k-cve-2018-0495.patch

# MinGW-specific patches.
# Rename *eay32.dll to lib*.dll
Patch1001:      mingw32-openssl-1.0.0-beta3-libversion.patch
# Fix engines/ install target after lib rename
Patch1002:      mingw32-openssl-1.0.2a-sfx.patch
# Some .c file contains in #include <dlfcn.h> while it
# doesn't really use anything from that header
Patch1003:      mingw-openssl-drop-unneeded-reference-to-dlfcn-h.patch
# Mingw-w64 compatibility patch
Patch1004:      openssl_mingw64_install_fix.patch
# Prevent a build failure which occurs because we don't have FIPS enabled
Patch1005:      mingw-openssl-fix-fips-build-failure.patch
# The function secure_getenv is a GNU extension which isn't available on Windows
Patch1006:      openssl-mingw64-dont-use-secure-getenv.patch
# Don't include the old winsock.h as it will cause warnings/errors in packages
# using the openssl headers like: Please include winsock2.h before windows.h
Patch1007:      openssl-dont-include-winsock-h.patch

BuildArch:      noarch
ExclusiveArch: %{ix86} x86_64

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-zlib

BuildRequires:  perl-interpreter
BuildRequires:  sed
BuildRequires:  /usr/bin/cmp
BuildRequires:  lksctp-tools-devel
BuildRequires:  /usr/bin/rename
BuildRequires:  /usr/bin/pod2man

# XXX Not really sure about this one.  The build script uses
# /usr/bin/makedepend which comes from imake.
BuildRequires:  imake

%if %{run_tests}
# Required both to build, and to run the tests.
# XXX This needs to be fixed - cross-compilation should not
# require running executables.
BuildRequires:  wine

# Required to run the tests.
BuildRequires:  xorg-x11-server-Xvfb
%endif


%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains Windows (MinGW) libraries and development tools.


# Win32
%package -n mingw32-openssl
Summary:        MinGW port of the OpenSSL toolkit
#Requires:       ca-certificates >= 2008-5
Requires:       pkgconfig

%description -n mingw32-openssl
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains Windows (MinGW) libraries and development tools.

%package -n mingw32-openssl-static
Summary:        Static version of the MinGW port of the OpenSSL toolkit
Requires:       mingw32-openssl = %{version}-%{release}

%description -n mingw32-openssl-static
Static version of the MinGW port of the OpenSSL toolkit.

# Win64
%package -n mingw64-openssl
Summary:        MinGW port of the OpenSSL toolkit
#Requires:       ca-certificates >= 2008-5
Requires:       pkgconfig

%description -n mingw64-openssl
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains Windows (MinGW) libraries and development tools.

%package -n mingw64-openssl-static
Summary:        Static version of the MinGW port of the OpenSSL toolkit
Requires:       mingw64-openssl = %{version}-%{release}

%description -n mingw64-openssl-static
Static version of the MinGW port of the OpenSSL toolkit.


%?mingw_debug_package


%prep
%setup -q -n openssl-%{version}

# The hobble_openssl is called here redundantly, just to be sure.
# The tarball has already the sources removed.
%{SOURCE1} > /dev/null

cp %{SOURCE12} %{SOURCE13} crypto/ec/

%patch1 -p1 -b .rpmbuild
%patch2 -p1 -b .defaults
%patch4 -p1 -b .enginesdir %{?_rawbuild}
%patch5 -p1 -b .no-rpath
%patch6 -p1 -b .use-localhost
%patch7 -p1 -b .timezone
%patch8 -p1 -b .perlfind %{?_rawbuild}
%patch9 -p1 -b .aliasing

%patch23 -p1 -b .default-paths
%patch24 -p1 -b .issuer-hash

%patch33 -p1 -b .ca-dir
%patch34 -p1 -b .x509
%patch35 -p1 -b .version-add-engines
#patch39 -p1 -b .ipv6-apps
%patch40 -p1 -b .fips
%patch43 -p1 -b .krb5keytab
%patch45 -p1 -b .env-zlib
%patch47 -p1 -b .warning
%patch49 -p1 -b .algo-doc
%patch50 -p1 -b .dtls1-abi
#patch51 -p1 -b .version
#patch56 -p1 -b .x931
%patch58 -p1 -b .md5-allow
%patch60 -p1 -b .dgst
#patch63 -p1 -b .starttls
%patch65 -p1 -b .chil
%patch66 -p1 -b .pkgconfig
#patch68 -p1 -b .secure-getenv
#patch70 -p1 -b .fips-ec
%patch71 -p1 -b .manfix
#patch72 -p1 -b .fips-ctor
%patch73 -p1 -b .suiteb
%patch74 -p1 -b .deprecate-algos
%patch75 -p1 -b .compat
#patch76 -p1 -b .fips-reqs
%patch77 -p1 -b .strength
%patch78 -p1 -b .cc-reqs
%patch90 -p1 -b .enc-fail
%patch94 -p1 -b .secp256k1
%patch95 -p1 -b .nistp224
%patch96 -p1 -b .speed-doc
%patch97 -p1 -b .no-ssl2
%patch98 -p1 -b .long-hello
#patch99 -p1 -b .randlock

%patch80 -p1 -b .wrap
%patch81 -p1 -b .padlock64
%patch82 -p1 -b .trusted-first
%patch83 -p1 -b .backports
%patch84 -p1 -b .ppc-update
%patch85 -p1 -b .req-x509
%patch86 -p1 -b .mont5-carry
%patch87 -p1 -b .ssl-err
%patch88 -p1 -b .rsaz-overflow
%patch89 -p1 -b .s390x-update
%patch100 -p1 -b .name-sensitive
%patch101 -p1 -b .overread
%patch102 -p1 -b .large-dh
%patch103 -p1 -b .gen-timing
%patch104 -p1 -b .asn1-recursive
%patch105 -p1 -b .rohnp-fix

# MinGW specific patches
%patch1001 -p1 -b .mingw-libversion
%patch1002 -p1 -b .mingw-sfx
%patch1003 -p0 -b .dlfcn
%patch1004 -p0 -b .mingw64
%patch1005 -p1 -b .fips_mingw
%patch1006 -p1 -b .secure_getenv_mingw
%patch1007 -p0 -b .winsock

sed -i 's/SHLIB_VERSION_NUMBER "1.0.0"/SHLIB_VERSION_NUMBER "%{version}"/' crypto/opensslv.h

# Modify the various perl scripts to reference perl in the right location.
perl util/perlpath.pl `dirname %{__perl}`

# Generate a table with the compile settings for my perusal.
touch Makefile
make TABLE PERL=%{__perl}

# Create two copies of the source folder as OpenSSL doesn't support out of source builds
mkdir ../build_win32
mv * ../build_win32
mv ../build_win32 .
mkdir build_win64
cp -Rp build_win32/* build_win64

# Use mingw cflags instead of hardcoded ones
sed -i -e '/^"mingw"/ s/-fomit-frame-pointer -O3 -march=i486 -Wall/%{mingw32_cflags}/' build_win32/Configure
sed -i -e '/^"mingw"/ s/-O3 -Wall/%{mingw64_cflags}/' build_win64/Configure


%build
###############################################################################
# Win32
###############################################################################
pushd build_win32

PERL=%{__perl} \
./Configure \
  --prefix=%{mingw32_prefix} \
  --openssldir=%{mingw32_sysconfdir}/pki/tls \
  zlib enable-camellia enable-seed enable-tlsext enable-rfc3779 \
  enable-cms enable-md2 enable-rc5 \
  no-mdc2 no-ec2m no-gost no-srp \
  no-fips no-hw \
  --cross-compile-prefix=%{mingw32_target}- \
  --enginesdir=%{mingw32_libdir}/openssl/engines \
  shared mingw

# Regenerate def files as we disabled some algorithms above
perl util/mkdef.pl crypto ssl update

make depend
make all build-shared

# Generate hashes for the included certs.
make rehash build-shared

popd

###############################################################################
# Win64
###############################################################################
pushd build_win64

PERL=%{__perl} \
./Configure \
  --prefix=%{mingw64_prefix} \
  --openssldir=%{mingw64_sysconfdir}/pki/tls \
  zlib enable-camellia enable-seed enable-tlsext enable-rfc3779 \
  enable-cms enable-md2 \
  no-mdc2 no-rc5 no-ec2m no-gost no-srp \
  no-fips no-hw \
  --cross-compile-prefix=%{mingw64_target}- \
  --enginesdir=%{mingw64_libdir}/openssl/engines \
  shared mingw64

# Regenerate def files as we disabled some algorithms above
perl util/mkdef.pl crypto ssl update

make depend
make all build-shared

# Generate hashes for the included certs.
make rehash build-shared

popd

# Clean up the .pc files
for i in build_win{32,64}/libcrypto.pc build_win{32,64}/libssl.pc build_win{32,64}/openssl.pc ; do
  sed -i '/^Libs.private:/{s/-L[^ ]* //;s/-Wl[^ ]* //}' $i
done


%if %{run_tests}
%check
#----------------------------------------------------------------------
# Run some tests.

# We must revert patch33 before tests otherwise they will fail
patch -p1 -R < %{PATCH33}

# This is a bit of a hack, but the test scripts look for 'openssl'
# by name.
pushd build_win32/apps
ln -s openssl.exe openssl
popd

# This is useful for diagnosing Wine problems.
WINEDEBUG=+loaddll
export WINEDEBUG

# Make sure we can find the installed DLLs.
WINEDLLPATH=%{mingw32_bindir}
export WINEDLLPATH

# The tests run Wine and require an X server (but don't really use
# it).  Therefore we create a virtual framebuffer for the duration of
# the tests.
# XXX There is no good way to choose a random, unused display.
# XXX Setting depth to 24 bits avoids bug 458219.
unset DISPLAY
display=:21
Xvfb $display -screen 0 1024x768x24 -ac -noreset & xpid=$!
trap "kill -TERM $xpid ||:" EXIT
sleep 3
DISPLAY=$display
export DISPLAY

make LDCMD=%{mingw32_cc} -C build_win32/test apps tests

# Disable this thread test, because we don't have pthread on Windows.
%{mingw32_cc} -o openssl-thread-test \
  -I./build_win32/include \
  %-{_mingw32_cflags} \
  %-{SOURCE8} \
  -L./build_win32 \
  -lssl -lcrypto \
  -lpthread -lz -ldl

## `krb5-config --cflags`
## `krb5-config --libs`
#
./openssl-thread-test --threads %{thread_test_threads}

#----------------------------------------------------------------------
%endif

# Add generation of HMAC checksum of the final stripped library
##define __spec_install_post \
#    #{?__debug_package:#{__debug_install_post}} \
#    #{__arch_install_post} \
#    #{__os_install_post} \
#    fips/fips_standalone_sha1 $RPM_BUILD_ROOT/#{_lib}/libcrypto.so.#{version} >$RPM_BUILD_ROOT/#{_lib}/.libcrypto.so.#{version}.hmac \
#    ln -sf .libcrypto.so.#{version}.hmac $RPM_BUILD_ROOT/#{_lib}/.libcrypto.so.#{soversion}.hmac \
##{nil}


%install
mkdir -p $RPM_BUILD_ROOT%{mingw32_libdir}/openssl
mkdir -p $RPM_BUILD_ROOT%{mingw32_bindir}
mkdir -p $RPM_BUILD_ROOT%{mingw32_includedir}
mkdir -p $RPM_BUILD_ROOT%{mingw32_mandir}

mkdir -p $RPM_BUILD_ROOT%{mingw64_libdir}/openssl
mkdir -p $RPM_BUILD_ROOT%{mingw64_bindir}
mkdir -p $RPM_BUILD_ROOT%{mingw64_includedir}
mkdir -p $RPM_BUILD_ROOT%{mingw64_mandir}

%mingw_make_install INSTALL_PREFIX=$RPM_BUILD_ROOT build-shared

# Install the file applink.c (#499934)
install -m644 build_win32/ms/applink.c $RPM_BUILD_ROOT%{mingw32_includedir}/openssl/applink.c
install -m644 build_win64/ms/applink.c $RPM_BUILD_ROOT%{mingw64_includedir}/openssl/applink.c

# I have no idea why it installs the manpages in /etc, but
# we remove them anyway.
rm -r $RPM_BUILD_ROOT%{mingw32_sysconfdir}/pki/tls/man
rm -r $RPM_BUILD_ROOT%{mingw64_sysconfdir}/pki/tls/man

# Set permissions on lib*.dll.a so that strip works.
chmod 0755 $RPM_BUILD_ROOT%{mingw32_libdir}/libcrypto.dll.a
chmod 0755 $RPM_BUILD_ROOT%{mingw32_libdir}/libssl.dll.a
chmod 0755 $RPM_BUILD_ROOT%{mingw64_libdir}/libcrypto.dll.a
chmod 0755 $RPM_BUILD_ROOT%{mingw64_libdir}/libssl.dll.a

# Install a makefile for generating keys and self-signed certs, and a script
# for generating them on the fly.
mkdir -p $RPM_BUILD_ROOT%{mingw32_sysconfdir}/pki/tls/certs
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{mingw32_sysconfdir}/pki/tls/certs/Makefile
install -m755 %{SOURCE6} $RPM_BUILD_ROOT%{mingw32_sysconfdir}/pki/tls/certs/make-dummy-cert
install -m755 %{SOURCE7} $RPM_BUILD_ROOT%{mingw32_sysconfdir}/pki/tls/certs/renew-dummy-cert

mkdir -p $RPM_BUILD_ROOT%{mingw64_sysconfdir}/pki/tls/certs
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{mingw64_sysconfdir}/pki/tls/certs/Makefile
install -m755 %{SOURCE6} $RPM_BUILD_ROOT%{mingw64_sysconfdir}/pki/tls/certs/make-dummy-cert
install -m755 %{SOURCE7} $RPM_BUILD_ROOT%{mingw64_sysconfdir}/pki/tls/certs/renew-dummy-cert

# Pick a CA script.
pushd $RPM_BUILD_ROOT%{mingw32_sysconfdir}/pki/tls/misc
mv CA.sh CA
popd

pushd $RPM_BUILD_ROOT%{mingw64_sysconfdir}/pki/tls/misc
mv CA.sh CA
popd

mkdir -m700 $RPM_BUILD_ROOT%{mingw32_sysconfdir}/pki/CA
mkdir -m700 $RPM_BUILD_ROOT%{mingw32_sysconfdir}/pki/CA/private

mkdir -m700 $RPM_BUILD_ROOT%{mingw64_sysconfdir}/pki/CA
mkdir -m700 $RPM_BUILD_ROOT%{mingw64_sysconfdir}/pki/CA/private

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-openssl.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-openssl.debugfiles


# Win32
%files -n mingw32-openssl -f mingw32-openssl.debugfiles
%doc build_win32/LICENSE
%{mingw32_bindir}/openssl.exe
%{mingw32_bindir}/c_rehash
%{mingw32_bindir}/libcrypto-%{soversion}.dll
%{mingw32_bindir}/libssl-%{soversion}.dll
%{mingw32_libdir}/libcrypto.dll.a
%{mingw32_libdir}/libssl.dll.a
%{mingw32_libdir}/engines
%{mingw32_libdir}/pkgconfig/*.pc
%{mingw32_includedir}/openssl
%config(noreplace) %{mingw32_sysconfdir}/pki

%files -n mingw32-openssl-static
%{mingw32_libdir}/libcrypto.a
%{mingw32_libdir}/libssl.a

# Win64
%files -n mingw64-openssl -f mingw64-openssl.debugfiles
%doc build_win64/LICENSE
%{mingw64_bindir}/openssl.exe
%{mingw64_bindir}/c_rehash
%{mingw64_bindir}/libcrypto-%{soversion}.dll
%{mingw64_bindir}/libssl-%{soversion}.dll
%{mingw64_libdir}/libcrypto.dll.a
%{mingw64_libdir}/libssl.dll.a
%{mingw64_libdir}/engines
%{mingw64_libdir}/pkgconfig/*.pc
%{mingw64_includedir}/openssl
%config(noreplace) %{mingw64_sysconfdir}/pki

%files -n mingw64-openssl-static
%{mingw64_libdir}/libcrypto.a
%{mingw64_libdir}/libssl.a


%changelog
* Mon Aug 19 2019 Victor Toso <victortoso@redhat.com> - 1.0.2k-2
- Remove not applied patchs from the source list
  Related: rhbz#1704077

* Fri Aug 24 2018 Christophe Fergeau <cfergeau@redhat.com> - 1.0.2k-1
- Sync with rhel 7.6 OpenSSL 1.0.2k+patches in order to get the latest security
  fixes
- Related: rhbz#1615874

* Tue Aug 14 2018 Victor Toso <victortoso@redhat.com> - 1.0.2h-7
- ExclusiveArch: i686, x86_64
- Related: rhbz#1615874

* Thu May 31 2018 Richard W.M. Jones <rjones@redhat.com> - 1.0.2h-6
- Remove mktemp build dependency, part of coreutils.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2h-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 1.0.2h-4
- Exclude *.debug files from non-debug packages

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2h-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2h-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May  7 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.2h-1
- Synced with native openssl-1.0.2h-1
- Fixes RHBZ #1332591 #1332589 #1330104 #1312861 #1312857 #1307773 #1302768

* Sat Feb  6 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.2f-1
- Synced with native openssl-1.0.2f-2
- Fixes RHBZ #1239685 #1290334 #1302768

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.2a-1
- Synced with native openssl-1.0.2a-1.fc23
- Fixes various CVE's (RHBZ #1203855 #1203856)

* Mon Dec 22 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1j-1
- Synced with native openssl-1.0.1j-3.fc22
- Add support for RFC 5649
- Prevent compiler warning "Please include winsock2.h before windows.h"
  when using the OpenSSL headers
- Fixes various CVE's (RHBZ #1127889 #1127709 #1152851)

* Thu Aug 21 2014 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.0.1i-1
- Synced with native openssl-1.0.1i-3.fc21
- Fixes various flaws (RHBZ#1096234 and RHBZ#1127705)
  CVE-2014-3505 CVE-2014-3506 CVE-2014-3507 CVE-2014-3511
  CVE-2014-3510 CVE-2014-3508 CVE-2014-3509 CVE-2014-0221
  CVE-2014-0198 CVE-2014-0224 CVE-2014-0195 CVE-2010-5298
  CVE-2014-3470

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1e-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr  9 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1e-6
- Synced patches with native openssl-1.0.1e-44.fc21
- Fixes CVE-2014-0160 (RHBZ #1085066)

* Sat Jan 25 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1e-5
- Synced patches with native openssl-1.0.1e-38.fc21
- Enable ECC support (RHBZ #1037919)
- Fixes CVE-2013-6450 (RHBZ #1047844)
- Fixes CVE-2013-4353 (RHBZ #1049062)
- Fixes CVE-2013-6449 (RHBZ #1045444)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1e-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 10 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1e-3
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Fri May 10 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1e-2
- Fix build of manual pages with current pod2man (#959439)

* Sun Mar 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1e-1
- Update to 1.0.1e (RHBZ #920868)
- Synced patches with native openssl-1.0.1e-4.fc19

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1c-2
- Fix FTBFS against latest pod2man

* Fri Nov  9 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1c-1
- Update to 1.0.1c
- Synced patches with native openssl-1.0.1c-7.fc19

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0d-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.0d-6
- Added win64 support

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 1.0.0d-5
- Pass the path to perl interpreter to Configure

* Tue Mar 06 2012 Kalev Lember <kalevlember@gmail.com> - 1.0.0d-4
- Renamed the source package to mingw-openssl (#800443)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.0d-3
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Apr 23 2011 Kalev Lember <kalev@smartlink.ee> - 1.0.0d-1
- Update to 1.0.0d
- Synced patches with Fedora native openssl-1.0.0d-2

* Fri Mar 04 2011 Kai Tietz <ktietz@redhat.com>
- Fixes for CVE-2011-0014 openssl: OCSP stapling vulnerability

* Thu Mar  3 2011 Kai Tietz <ktietz@redhat.com> - 1.0.0a-3
- Bump and rebuild.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jun 19 2010 Kalev Lember <kalev@smartlink.ee> - 1.0.0a-1
- Updated to openssl 1.0.0a
- Synced patches with Fedora native openssl-1.0.0a-1
- Use sed to fix up cflags instead of unmaintainable patch
- Rebased mingw32 specific patches
- Disabled capieng to fix build
- Properly regenerate def files with mkdef.pl and drop linker-fix.patch

* Thu Nov 26 2009 Kalev Lember <kalev@smartlink.ee> - 1.0.0-0.6.beta4
- Merged patches from native Fedora openssl (up to 1.0.0-0.16.beta4)
- Dropped the patch to fix non-fips mingw build,
  as it's now merged into fips patch from native openssl

* Sun Nov 22 2009 Kalev Lember <kalev@smartlink.ee> - 1.0.0-0.5.beta4
- Updated to version 1.0.0 beta 4
- Merged patches from native Fedora openssl (up to 1.0.0-0.15.beta4)
- Added patch to fix build with fips disabled

* Fri Sep 18 2009 Kalev Lember <kalev@smartlink.ee> - 1.0.0-0.4.beta3
- Rebuilt to fix debuginfo

* Sun Aug 30 2009 Kalev Lember <kalev@smartlink.ee> - 1.0.0-0.3.beta3
- Simplified the lib renaming patch

* Sun Aug 30 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.0-0.2.beta3
- Fixed invalid RPM Provides

* Fri Aug 28 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.0-0.1.beta3
- Update to version 1.0.0 beta 3
- Use %%global instead of %%define
- Automatically generate debuginfo subpackage
- Merged various changes from the native Fedora package (up to 1.0.0-0.5.beta3)
- Don't use the %%{_mingw32_make} macro anymore as it's ugly and causes side-effects
- Added missing BuildRequires mingw32-dlfcn (Kalev Lember)
- Reworked patches to rename *eay32.dll to lib*.dll (Kalev Lember)
- Patch Configure script to use %%{_mingw32_cflags} (Kalev Lember)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8j-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May  9 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.8j-6
- Add the file include/openssl/applink.c to the package (BZ #499934)

* Tue Apr 14 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.8j-5
- Fixed %%defattr line
- Added -static subpackage

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8j-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 0.9.8j-3
- Rebuild for mingw32-gcc 4.4

* Mon Feb  2 2009 Levente Farkas <lfarkas@lfarkas.org> - 0.9.8j-2
- Various build fixes.

* Wed Jan 28 2009 Levente Farkas <lfarkas@lfarkas.org> - 0.9.8j-1
- update to new upstream version.

* Mon Dec 29 2008 Levente Farkas <lfarkas@lfarkas.org> - 0.9.8g-2
- minor cleanup.

* Tue Sep 30 2008 Richard W.M. Jones <rjones@redhat.com> - 0.9.8g-1
- Initial RPM release.
