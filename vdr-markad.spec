Name:           vdr-markad
Version:        3.0.10
Release:        1%{?dist}
Summary:        Advanced commercial detection for VDR
License:        GPLv2+
URL:            https://github.com/kfb77/vdr-plugin-markad
Source0:        https://github.com/kfb77/vdr-plugin-markad/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= 1.7.30
BuildRequires:  ffmpeg-devel >= 4.1
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
VDR-Plugin: markad - %{summary}

%prep
%autosetup -p 1 -n vdr-plugin-markad-%{version}

sed -i -e 's|$(DESTDIR)/var/lib/markad|$(DESTDIR)%{vdr_vardir}/markad/|' command/Makefile
sed -i -e 's|/LC_MESSAGES/markad.mo|/LC_MESSAGES/vdr-markad.mo|' command/Makefile

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" all

%install
%make_install

install -dm 755 %{buildroot}%{vdr_plugindir}
install -Dpm 644 %{SOURCE1} \
  %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/markad.conf

%find_lang %{name}

%post
# make sure /etc/services has a svdrp entry
if ! grep E '\<svdrp\>' /etc/services > /dev/null 2>&1 ; then
  echo "svdrp         6419/tcp                          # VDR" >> /etc/services
fi

%files -f %{name}.lang
%doc COPYING README HISTORY
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/markad.conf
%{_mandir}/man1/markad.1.*
%{_bindir}/markad
%{_libdir}/vdr/libvdr-markad.so.%{vdr_apiversion}
%{vdr_vardir}/markad/

%changelog
* Tue Aug 17 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.10-1
- Update to 3.0.10

* Tue Aug 17 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.9-1
- Update to 3.0.9

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 23 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.8-1
- Update to 3.0.8

* Wed Jul 14 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.7-1
- Update to 3.0.7

* Wed Jun 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.6-1
- Update to 3.0.6

* Wed Jun 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.5-1
- Update to 3.0.5

* Sat Jun 05 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.4-1
- Update to 3.0.4

* Sun May 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.3-1
- Update to 3.0.3

* Sun May 09 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Wed May 05 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1

* Mon Apr 26 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.0-2
- Rebuilt for new VDR API version

* Sat Apr 24 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Thu Apr 22 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.6.8-1
- Update to 2.6.8

* Sat Mar 27 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.6.7-1
- Update to 2.6.7

* Sat Mar 13 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.6.6-1
- Update to 2.6.6

* Sat Mar 06 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.6.5-1
- Update to 2.6.5

* Thu Mar 04 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.6.4-1
- Update to 2.6.4

* Fri Feb 26 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.6.3-1
- Update to 2.6.3

* Tue Feb 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2

* Thu Feb 04 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0

* Sat Jan 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.5.6-1
- Update to 2.5.6

* Mon Jan 18 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.5.3-1
- Update to 2.5.3

* Fri Jan 08 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.5.2-1
- Update to 2.5.2

* Mon Jan 04 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.5.1-2
- Rebuilt for new VDR API version

* Fri Jan 01 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1

* Thu Dec 24 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0

* Sat Dec 19 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.4.4-1
- Update to 2.4.4

* Fri Dec 04 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.4.3-1
- Update to 2.4.3

* Wed Oct 21 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2
- Rebuilt for new VDR API version

* Thu Sep 17 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Sun Aug 30 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.3.6-1
- Update to 2.3.6

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.3.4-3
- Rebuilt for new VDR API version

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.3.4-1
- Update to 2.3.4

* Tue Jul 14 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3

* Mon May 25 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Sat May 16 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4

* Sun May 03 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.0.3-1
- Switched URL to https://github.com/kfb77/vdr-plugin-markad
- Update to 2.0.3
- Dropped 03-markad-decoder-V1-00.diff

* Fri Mar 13 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-33.20170313gitea2e182
- Replace 03-markad-decoder-V0-59.diff by 03-markad-decoder-V0-59.diff
- Dropped 00-markad-libavcodec58-V0-02.diff
- Dropped 01-markad-Makefile-V0-06.diff
- Dropped 02-markad-deprecated-V0-05.diff

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.1.4-32.20170313gitea2e182
- Rebuild for ffmpeg-4.3 git

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.4-31.20170313gitea2e182
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-30.20170313gitea2e182
- Replace 00-markad-libavcodec58-V0-01.diff by 00-markad-libavcodec58-V0-02.diff
- Replace 02-deprecated-V0-04.diff by 02-markad-deprecated-V0-05.diff
- Replace 03-markad-decoder-V0-31.diff by 03-markad-decoder-V0-59.diff

* Sun Dec 15 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-29.20170313gitea2e182
- Replace 03-markad-decoder-V0-31.diff by 03-markad-decoder-V0-50.diff

* Thu Dec 05 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-28.20170313gitea2e182
- Replace 03-markad-decoder-V0-24.diff by 03-markad-decoder-V0-31.diff

* Tue Dec 03 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-27.20170313gitea2e182
- Cleanup spec file

* Tue Dec 03 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-26.20170313gitea2e182
- Dropped vdr-markad-ffmpeg4-fix.patch
- Add 00-markad-libavcodec58-V0-01.diff
- Add 01-markad-Makefile-V0-06.diff
- Add 02-deprecated-V0-04.diff
- Add 04-markad-decoder-V0-24.diff

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 0.1.4-25.20170313gitea2e182
- Rebuild for new ffmpeg version

* Mon Jul 01 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-24.20170313gitea2e182
- Rebuilt for new VDR API version 2.4.1

* Sun Jun 30 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-23.20170313gitea2e182
- Rebuilt for new VDR API version

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-22.20170313gitea2e182
- Rebuilt for new VDR API version

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.4-21.20170313gitea2e182
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-20.20170313gitea2e182
- Add vdr-markad-ffmpeg4-fix.patch
- Spec file cleanup

* Thu Oct 11 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-19.20170313gitea2e182
- Add BR gcc-c++

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.1.4-18.20170313gitea2e182
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.4-17.20170313gitea2e182
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.1.4-16.20170313gitea2e182
- Use compat-ffmpeg28 for F28

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.1.4-15.20170313gitea2e182
- Rebuilt for ffmpeg-3.5 git

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.1.4-14.20170313gitea2e182
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 30 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.1.4-13.20170313gitea2e182
- Rebuild for ffmpeg update

* Fri Mar 24 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-12.20170313gitea2e182
- rebuild for new git version

* Mon Sep 26 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-11.20160925git3681d3a
- rebuild for new git version

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.1.4-10.20151016git74e2a8c
- Rebuilt for ffmpeg-3.1.1

* Wed Jun 29 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-9.20151016git74e2a8c
- replaced function avcodec_alloc_frame(); by av_frame_alloc(); due ffmpeg3 version

* Sat Oct 17 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-8.20151016git74e2a8c
- rebuild for new git version

* Fri Oct 02 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-7.20150926git5345436
- rebuild for new git version

* Mon Oct 20 2014 Sérgio Basto <sergio@serjux.com> - 0.1.4-6.20140902gitc55f43f
- Rebuilt for FFmpeg 2.4.3

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

