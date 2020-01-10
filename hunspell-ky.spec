Name: hunspell-ky
Summary: Kirghiz hunspell dictionaries
%define upstreamid 20090415
Version: 0.%{upstreamid}
Release: 7%{?dist}
Group: Applications/Text
Source: http://ftp.gnu.org/gnu/aspell/dict/ky/aspell6-ky-0.01-0.tar.bz2
URL: http://borel.slu.edu/crubadan/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch
BuildRequires: aspell, hunspell-devel

Requires: hunspell

%description
Kirghiz hunspell dictionaries.

%prep
%setup -q -n aspell6-ky-0.01-0

%build
export LANG=ky_KG.utf8
preunzip -d *.cwl
cat *.wl > kirghiz.wordlist
wordlist2hunspell kirghiz.wordlist ky_KG
cp -p ky_affix.dat ky_KG.aff

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING Copyright README doc/Crawler.txt
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090415-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090415-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090415-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090415-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090415-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090414-2
- preserve timestamp

* Mon Jun 22 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090415-1
- out by one

* Thu Jun 18 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090414-1
- initial version
