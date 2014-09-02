%global commit c55f43f413dff8740f99d684e8879835d4409920
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20140902

Name:           vdr-markad
Version:        0.1.4
Release:        5.%{gitdate}git%{shortcommit}%{?dist}
Summary:        Advanced commercial detection for VDR
License:        GPLv2+
# how to get the tarball
# go to http://projects.vdr-developer.org/git/vdr-plugin-markad.git/commit/
# click the link behind commit, then select the download links below.
URL:            http://projects.vdr-developer.org/projects/plg-markad
Source0:        http://projects.vdr-developer.org/git/vdr-plugin-markad.git/snapshot/vdr-plugin-markad-%{commit}.tar.bz2
Source1:        %{name}.conf

BuildRequires:  vdr-devel >= 1.7.30
BuildRequires:  ffmpeg-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
VDR-Plugin: markad - %{summary}

%prep
%setup -qn vdr-plugin-markad-%{commit}

%build
make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" %{?_smp_mflags} \
    LIBDIR=. VDRDIR=%{_libdir}/vdr VDRINCDIR=%{_includedir} \
    LOCALEDIR=./locale all

%install
install -dm 755 $RPM_BUILD_ROOT%{vdr_plugindir}
install -pm 755 plugin/libvdr-markad.so.%{vdr_apiversion} $RPM_BUILD_ROOT%{vdr_plugindir}
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/markad.conf

install -dm 755 $RPM_BUILD_ROOT%{_bindir}
install -pm 755 command/markad $RPM_BUILD_ROOT%{_bindir}

# locale
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/locale
cp -pR plugin/locale/* $RPM_BUILD_ROOT%{_datadir}/locale

# copy logos
install -dm 755 $RPM_BUILD_ROOT%{vdr_vardir}/markad/logos
cp -pR command/logos/* $RPM_BUILD_ROOT%{vdr_vardir}/markad/logos

# install man
pushd command
make install-doc DESTDIR=$RPM_BUILD_ROOT
popd

%find_lang %{name}

%post
# make sure /etc/services has a svdrp entry
if ! grep E '\<svdrp\>' /etc/services > /dev/null 2>&1 ; then
  echo "svdrp         6419/tcp                          # VDR" >> /etc/services
fi

%files -f %{name}.lang
%doc COPYING README HISTORY
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/markad.conf
%{_mandir}/man1/markad.1.gz
%{_bindir}/markad
%{_libdir}/vdr/libvdr-markad.so.%{vdr_apiversion}
%{vdr_vardir}/markad/

%changelog
* Tue Sep 02 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-5.20140902gitc55f43f
- rebuild for new git version

* Fri May 02 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-4.20140421git3c99d47
- removed %%config(noreplace) flag in %%file section for logo dir
- added  %%{optflags} macro in build section

* Mon Apr 21 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-3.20140421git3c99d47
- rebuild for new git version

* Sun Jan 19 2014 Martin Gansser <linux4martin@gmx.de> - 0.1.4-2.20131115git09617a6
- added gitdate for fedora naming schema
- added tarball download instructions

* Fri Jan 10 2014 Martin Gansser <linux4martin@gmx.de> - 0.1.4-1.09617a6
- rebuild for new git version

* Tue Sep 25 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.4-2
- used macro pname in file section
- added manpage patch

* Mon Sep 24 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.4-1
- rebuild for new release

* Tue May 22 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.3-8.20120522git
- new git release
- removed readme patch

* Sat May 19 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.3-7.20120519git
- new git release
- added plugin option file
- added patch for readme file

* Tue May 15 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.3-6.20120504git
- added correct permissions for vdr_vardir

* Sun May 13 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.3-5.20120504git
- fixed unstripped-binary-or-object messages
- fsf-address upstream bug
- fixed dependencies

* Tue May 08 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.3-4.20120504git
- solved unstripped-binary-or-object
- removed warning deprecated-grep
- removed mixed-use-of-spaces-and-tabs
- removed unneeded global settings
- added path for tv logos

* Mon May 07 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.3-3.20120504git
- added svdrp to /etc/services
- removed defattr in file section

* Sun May 06 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.3-2.20120504git
- new git version
- changed name of source package

* Sun Apr 29 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.3-1.20120310git
- first build for fc17

* Wed Sep 21 2011 Sebastian Vahl <fedora@deadbabylon.de> - 0.1.2-1
- initial release

