%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.01-1
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Upper Sorbian
%define languagecode hsb
%define lc_ctype hsb_DE

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.01.1
Release:       %mkrel 11
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:      aspell-%{lc_ctype}

Autoreqprov:   no

%description
An %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 Copyright README* 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright 
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.01.1-10mdv2011.0
+ Revision: 662837
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 0.01.1-9mdv2011.0
+ Revision: 603217
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.01.1-8mdv2010.1
+ Revision: 518930
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.01.1-7mdv2010.0
+ Revision: 413073
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.01.1-6mdv2009.1
+ Revision: 350036
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.01.1-5mdv2009.0
+ Revision: 220385
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.01.1-4mdv2008.1
+ Revision: 182473
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.01.1-3mdv2008.1
+ Revision: 148796
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.01.1-2mdv2007.0
+ Revision: 123271
- Import aspell-hsb

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.01.1-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Thu Jun 29 2006 Pablo Saratxaga <pablo@mandriva.com> 0.01.1-2mdk
- rebuilt to require locales-hsb, now available

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandriva.com> 0.01.1-1mdk
- first version

