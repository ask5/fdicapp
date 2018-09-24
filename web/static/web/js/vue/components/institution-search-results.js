var InstitutionSearchResultItem =  Vue.component('institution-search-result-item', {
    props: ['item'],
    template: '<li>{{ item._source.cert }} - {{ item._source.name }}</li>'
});