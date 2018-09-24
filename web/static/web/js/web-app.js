
const app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#main',
    data: {
        term: '',
        institutions:[],
        noResults:false,
		searching:false
    },
    methods:{
        search: function(){
            this.searching = true;
            var match = [];
            if (isNaN(this.term)){
                match.push({ "match": { "name": this.term }});
            }else{
                match.push({ "match": { "name": this.term }});
                match.push({ "match": { "cert":  this.term }});
            }
            fetch('/es/institutions', {
                method: 'post',
                body: JSON.stringify({
                        "query": {
                            "bool": {
                                  "should": match
                                }
                        }
                    })
            }).then(response => response.json())
            .then(json => {
                this.institutions = json.hits.hits;
                this.searching = false;
                this.noResults = json.hits.hits.length === 0;
            });
        }
    }
});

