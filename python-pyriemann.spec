%global modname pyriemann

Name:           python-%{modname}
Version:        0.2.3
Release:        1%{?dist}
Summary:        Covariance matrices manipulation and Biosignal classification

License:        BSD
URL:            https://github.com/alexandrebarachant/pyRiemann
Source0:        https://github.com/alexandrebarachant/pyRiemann/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
pyriemann is a python package for covariance matrices manipulation and
classification through riemannian geometry.

The primary target is classification of multivariate biosignals,
like EEG, MEG or EMG.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-nose
BuildRequires:  numpy scipy
BuildRequires:  python-scikit-learn
BuildRequires:  python-joblib
BuildRequires:  python2-pandas
BuildRequires:  python-matplotlib
Requires:       numpy scipy
Requires:       python-scikit-learn
Requires:       python-joblib
Requires:       python2-pandas
Requires:       python-matplotlib

%description -n python2-%{modname}
pyriemann is a python package for covariance matrices manipulation and
classification through riemannian geometry.

The primary target is classification of multivariate biosignals,
like EEG, MEG or EMG.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  /usr/bin/2to3
BuildRequires:  python3-nose
BuildRequires:  python3-numpy python3-scipy
BuildRequires:  python3-scikit-learn
BuildRequires:  python3-joblib
BuildRequires:  python3-pandas
BuildRequires:  python3-matplotlib
Requires:       python3-numpy python3-scipy
Requires:       python3-scikit-learn
Requires:       python3-joblib
Requires:       python3-pandas
Requires:       python3-matplotlib

%description -n python3-%{modname}
pyriemann is a python package for covariance matrices manipulation and
classification through riemannian geometry.

The primary target is classification of multivariate biosignals,
like EEG, MEG or EMG.

Python 3 version.

%prep
%autosetup -c
mv pyRiemann-%{version} python2
cp -a python2 python3
2to3 --write --nobackups python3/

%build
pushd python2
  %py2_build
popd
pushd python3
  %py3_build
popd

%install
pushd python2
  %py2_install
popd
pushd python3
  %py3_install
popd

%check
pushd python2/tests
  PYTHONPATH=%{buildroot}%{python2_sitelib} nosetests-%{python2_version} -v
popd
pushd python3/tests
  PYTHONPATH=%{buildroot}%{python3_sitelib} nosetests-%{python3_version} -v
popd

%files -n python2-%{modname}
%license python2/LICENSE
%doc python2/README.md python2/examples
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%license python3/LICENSE
%doc python3/README.md python3/examples
%{python3_sitelib}/%{modname}*

%changelog
* Wed Nov 11 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2.3-1
- Initial package
