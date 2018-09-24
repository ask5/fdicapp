var InstitutionSearch =  Vue.component('institution-search', {
    data: function () {
        return {
            query: undefined,
            searching: false,
            errors:[],
            results: []
        }
    },
    methods:{
        search: function () {
            if(this.query) {
                this.errors.length = 0;
                this.searching = true;
                var match = [];
                if (isNaN(this.query)) {
                    match.push({"match": {"name": this.query}});
                } else {
                    match.push({"match": {"name": this.query}});
                    match.push({"match": {"cert": this.query}});
                }
                fetch('/els/institutions', {
                    method: 'post',
                    body: JSON.stringify({
                        "query": {
                            "bool": {
                                "should": match
                            }
                        }
                    })
                }).then(
                    response => response.json()
                ).then(
                    json => {
                        this.results = json.hits.hits;
                        this.searching = false;
                    }
                ).catch(
                    e => {
                        this.errors.push(e);
                        this.searching = false;
                    }
                );
            }
        }
    },
    template: '<div> \
        <input v-model="query" type="search"> \
        <button @click="search">Search</button> \
        <ul>\
        <li v-for="e in errors">{{ e.message }}</li>\
        </ul>\
        <ul> \
        <institution-search-result-item \
                v-for="r in results" \
                v-bind:item="r" \
                v-bind:key="r._source.cert"> \
            </institution-search-result-item> \
        </ul> \
        </div>'
});