#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pbkrtest
Version  : 0.5.2
Release  : 92
URL      : https://cran.r-project.org/src/contrib/pbkrtest_0.5.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pbkrtest_0.5.2.tar.gz
Summary  : Parametric Bootstrap, Kenward-Roger and Satterthwaite Based
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-broom
Requires: R-dplyr
Requires: R-lme4
Requires: R-numDeriv
BuildRequires : R-Rcpp
BuildRequires : R-broom
BuildRequires : R-dplyr
BuildRequires : R-lme4
BuildRequires : R-numDeriv
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Kenward-Rogers degree of freedom methods and (b) parametric bootstrap
    for mixed effects models as implemented in the 'lme4'
    package. Implements parametric bootstrap test for generalized linear
    mixed models as implemented in 'lme4' and generalized linear
    models. The package is documented in the paper by Halekoh and

%prep
%setup -q -n pbkrtest
cd %{_builddir}/pbkrtest

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1674167343

%install
export SOURCE_DATE_EPOCH=1674167343
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/pbkrtest/NEWS
/usr/lib64/R/library/pbkrtest/R/pbkrtest
/usr/lib64/R/library/pbkrtest/R/pbkrtest.rdb
/usr/lib64/R/library/pbkrtest/R/pbkrtest.rdx
/usr/lib64/R/library/pbkrtest/WORDLIST
/usr/lib64/R/library/pbkrtest/data/Rdata.rdb
/usr/lib64/R/library/pbkrtest/data/Rdata.rds
/usr/lib64/R/library/pbkrtest/data/Rdata.rdx
/usr/lib64/R/library/pbkrtest/doc/a01-pbkrtest.R
/usr/lib64/R/library/pbkrtest/doc/a01-pbkrtest.html
/usr/lib64/R/library/pbkrtest/doc/a01-pbkrtest.rmd
/usr/lib64/R/library/pbkrtest/doc/a02-coercion.R
/usr/lib64/R/library/pbkrtest/doc/a02-coercion.html
/usr/lib64/R/library/pbkrtest/doc/a02-coercion.rmd
/usr/lib64/R/library/pbkrtest/doc/index.html
/usr/lib64/R/library/pbkrtest/help/AnIndex
/usr/lib64/R/library/pbkrtest/help/aliases.rds
/usr/lib64/R/library/pbkrtest/help/paths.rds
/usr/lib64/R/library/pbkrtest/help/pbkrtest.rdb
/usr/lib64/R/library/pbkrtest/help/pbkrtest.rdx
/usr/lib64/R/library/pbkrtest/html/00Index.html
/usr/lib64/R/library/pbkrtest/html/R.css
