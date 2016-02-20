%global pkg_name maven-filtering
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:             %{?scl_prefix}%{pkg_name}
Version:          1.1
Release:          3.10%{?dist}
Summary:          Shared component providing resource filtering
License:          ASL 2.0
URL:              http://maven.apache.org/shared/%{pkg_name}/index.html
Source0:          http://repo1.maven.org/maven2/org/apache/maven/shared/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip
BuildArch:        noarch

BuildRequires:    %{?scl_prefix_java_common}maven-local
BuildRequires:    maven30-maven-shared
BuildRequires:    maven30-plexus-build-api
BuildRequires:    maven30-plexus-containers-component-metadata


%description
These Plexus components have been built from the filtering process/code in 
Maven Resources Plugin. The goal is to provide a shared component for all 
plugins that needs to filter resources.

%package javadoc
Summary:          Javadoc for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x

# Replace plexus-maven-plugin with plexus-component-metadata
%pom_xpath_set "pom:plugin[pom:artifactId[text()='plexus-maven-plugin']]//pom:goal[text()='descriptor']" generate-metadata
%pom_xpath_set "pom:artifactId[text()='plexus-maven-plugin']" plexus-component-metadata
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
# Tests use a package that is no longer present in plexus-build-api (v0.0.7)
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%doc DEPENDENCIES LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.1-3.10
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-3.9
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.1-3.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.1-3.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-3.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-3.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-3.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-3.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-3.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-3.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1-3
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-2
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-1
- Update to upstream version 1.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-10
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Nov 27 2012 Tomas Radej <tradej@redhat.com> - 1.0-9
- Added NOTICE to javadoc

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 15 2012 Tomas Radej <tradej@redhat.com> - 1.0-7
- Replaced plexus-maven-plugin with plexus-containers-component-metadata

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 31 2011 Tomas Radej <tradej@redhat.com> - 1.0-5
- Really fixed Provides/Obsoletes

* Wed Aug 31 2011 Tomas Radej <tradej@redhat.com> - 1.0-4
- Fixed Provides/Obsoletes

* Wed Aug 31 2011 Tomas Radej <tradej@redhat.com> - 1.0-3
- Added Provides/Obsoletes

* Tue Aug 16 2011 Tomas Radej <tradej@redhat.com> 1.0-2
- Removed rm -rf {buildroot}

* Tue Aug 16 2011 Tomas Radej <tradej@redhat.com> 1.0-1
- Initial release (thanks to the GULaG team)

