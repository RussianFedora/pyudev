%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define use_git 0
%define pyudev_version 0.11
%define git_version git20110715

Summary:       Python binding for libudev
Name:          pyudev
%if %use_git
Version:       %{pyudev_version}.%{git_version}
%else
Version:       %{pyudev_version}
%endif
Release:       1%{?dist}.R

License:       LGPLv2+
Group:         Development/Languages
URL:           http://packages.python.org/pyudev
%if %use_git
Source:        %{name}-%{version}.tar.bz2
%else
Source:        http://pypi.python.org/packages/source/p/pyudev/pyudev-%{version}.tar.gz
%endif
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: python-devel python-setuptools libudev-devel

Requires:      python-apipkg
Requires:      udev

BuildArch:     noarch


%description
pyudev is a Python binding for libudev.


%package qt4
Group:        Development/Languages
Summary:      PyQt4 binding for libudev
Requires:     %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:     PyQt4


%description qt4
pyudev is a Python binding for libudev.

This package provides the PyQt4 binding.


%prep
%setup -q


%build
python setup.py build


%install
rm -rf %{buildroot}

python setup.py install -O1 --skip-build \
   --root=%{buildroot} \
   --install-headers=%{_includedir}/python \
   --install-lib=%{python_sitelib} \
   --single-version-externally-managed


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc CHANGES.rst COPYING README.rst
%{python_sitelib}/pyudev/*
%if %use_git
%{python_sitelib}/pyudev-%{pyudev_version}*-py?.?.egg-info/*
%else
%{python_sitelib}/pyudev-%{pyudev_version}-py?.?.egg-info/*
%endif
%exclude %{python_sitelib}/pyudev/*qt*


%files qt4
%defattr(-,root,root)
%{python_sitelib}/pyudev/*qt*


%changelog
* Mon Jul 25 2011 Alexei Panov <elemc AT atisserv DOT ru> - 0.11-1.R
- new version
- change spec for using git versions
* Wed Feb  9 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.8-1
- initial build for Fedora
