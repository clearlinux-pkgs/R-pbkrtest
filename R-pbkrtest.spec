#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pbkrtest
Version  : 0.4.7
Release  : 52
URL      : http://cran.r-project.org/src/contrib/pbkrtest_0.4-7.tar.gz
Source0  : http://cran.r-project.org/src/contrib/pbkrtest_0.4-7.tar.gz
Summary  : Parametric Bootstrap and Kenward Roger Based Methods for Mixed
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-lme4
BuildRequires : R-Rcpp
BuildRequires : R-lme4
BuildRequires : clr-R-helpers

%description
as implemented in the 'lme4' package. This package implements a parametric
    bootstrap test and a Kenward Roger modification of F-tests for linear mixed
    effects models and a parametric bootstrap test for generalized linear mixed
    models.

%prep
%setup -q -c -n pbkrtest

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502416876

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1502416876
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbkrtest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbkrtest
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library pbkrtest
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || : || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pbkrtest/CITATION
/usr/lib64/R/library/pbkrtest/DESCRIPTION
/usr/lib64/R/library/pbkrtest/INDEX
/usr/lib64/R/library/pbkrtest/Meta/Rd.rds
/usr/lib64/R/library/pbkrtest/Meta/data.rds
/usr/lib64/R/library/pbkrtest/Meta/features.rds
/usr/lib64/R/library/pbkrtest/Meta/hsearch.rds
/usr/lib64/R/library/pbkrtest/Meta/links.rds
/usr/lib64/R/library/pbkrtest/Meta/nsInfo.rds
/usr/lib64/R/library/pbkrtest/Meta/package.rds
/usr/lib64/R/library/pbkrtest/Meta/vignette.rds
/usr/lib64/R/library/pbkrtest/NAMESPACE
/usr/lib64/R/library/pbkrtest/R/pbkrtest
/usr/lib64/R/library/pbkrtest/R/pbkrtest.rdb
/usr/lib64/R/library/pbkrtest/R/pbkrtest.rdx
/usr/lib64/R/library/pbkrtest/data/beets.RData
/usr/lib64/R/library/pbkrtest/data/budworm.RData
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
