#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pbkrtest
Version  : 0.4
Release  : 21
URL      : http://cran.r-project.org/src/contrib/pbkrtest_0.4-2.tar.gz
Source0  : http://cran.r-project.org/src/contrib/pbkrtest_0.4-2.tar.gz
Summary  : Parametric bootstrap and Kenward-Roger-based methods for mixed
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-lme4
BuildRequires : R-Rcpp
BuildRequires : R-lme4
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n pbkrtest

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library pbkrtest
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library pbkrtest


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pbkrtest/CITATION
/usr/lib64/R/library/pbkrtest/DESCRIPTION
/usr/lib64/R/library/pbkrtest/INDEX
/usr/lib64/R/library/pbkrtest/Meta/Rd.rds
/usr/lib64/R/library/pbkrtest/Meta/data.rds
/usr/lib64/R/library/pbkrtest/Meta/hsearch.rds
/usr/lib64/R/library/pbkrtest/Meta/links.rds
/usr/lib64/R/library/pbkrtest/Meta/nsInfo.rds
/usr/lib64/R/library/pbkrtest/Meta/package.rds
/usr/lib64/R/library/pbkrtest/Meta/vignette.rds
/usr/lib64/R/library/pbkrtest/NAMESPACE
/usr/lib64/R/library/pbkrtest/R/pbkrtest
/usr/lib64/R/library/pbkrtest/R/pbkrtest.rdb
/usr/lib64/R/library/pbkrtest/R/pbkrtest.rdx
/usr/lib64/R/library/pbkrtest/data/beets.txt.gz
/usr/lib64/R/library/pbkrtest/data/budworm.txt.gz
/usr/lib64/R/library/pbkrtest/doc/index.html
/usr/lib64/R/library/pbkrtest/doc/pbkrtest-introduction.R
/usr/lib64/R/library/pbkrtest/doc/pbkrtest-introduction.Rnw
/usr/lib64/R/library/pbkrtest/doc/pbkrtest-introduction.pdf
/usr/lib64/R/library/pbkrtest/help/AnIndex
/usr/lib64/R/library/pbkrtest/help/aliases.rds
/usr/lib64/R/library/pbkrtest/help/paths.rds
/usr/lib64/R/library/pbkrtest/help/pbkrtest.rdb
/usr/lib64/R/library/pbkrtest/help/pbkrtest.rdx
/usr/lib64/R/library/pbkrtest/html/00Index.html
/usr/lib64/R/library/pbkrtest/html/R.css
