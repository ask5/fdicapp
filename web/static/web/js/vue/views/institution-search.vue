        <input v-model="term" type="search">
        <button @click="search">Search</button>
        <hr>
        <div v-if="noResults">
			Sorry, but no results were found.
		</div>
        <div v-else>
            [[ institutions.length ]] Institution(s) found.
        </div>
		<div v-if="searching">
		    <i>Searching...</i>
		</div>
        <ul>
            <institution-search-result-item
                v-for="i in institutions"
                v-bind:i="i"
                v-bind:key="i._source.cert">
            </institution-search-result-item>
        </ul>
