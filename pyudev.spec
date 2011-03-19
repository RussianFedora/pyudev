%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary:       Python binding for libudev
Name:          pyudev
Version:       0.8
Release:       1%{?dist}

License:       LGPLv2+
Group:         Development/Languages
URL:           http://packages.python.org/pyudev
Source:        http://pypi.python.org/packages/source/p/pyudev/pyudev-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: python-devel

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
%{python_sitelib}/pyudev-0.8-py?.?.egg-info/*
%exclude %{python_sitelib}/pyudev/*qt*


%files qt4
%defattr(-,root,root)
%{python_sitelib}/pyudev/*qt*


%changelog
* Wed Feb  9 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.8-1
- initial build for Fedora
