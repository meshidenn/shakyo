/* global $, _, crossfilter, d3 */
(function(nbviz) {
    'use strict';
    var query_winners = "winners?projection=" + 
        JSON.stringify( {"mini_bio":0, "bio_image": 0} );

    var q = queue()
        .defer(d3.json, "static/data/world-110m.json")
        .defer(d3.csv, "static/data/world-country-names-nobel.csv")
        .defer(d3.json, "static/data/winning_country_data.json")

        // the $static_api flag dictates whether we are using static
        // files or using the mongodb based eve-api
        //if(window.$STATIC_API){
        //    q.defer(nbviz.getDataFromAPI, '_winners');
        //}
        //else {
        //    q.defer(nbviz.getDataFromAPI, query_winners);
        //}
        q.defer(nbviz.getDataFromAPI, query_winners);
        q.await(ready);

    function ready(error, worldMap, countryNames, countryData, winnersData) {
        if(error){
            return console.warn(error);
        }
        nbviz.data.countryData = countryData;
        nbviz.makeFilterAndDimensions(winnersData);
        nbviz.initMenu();
        nbviz.initMap(worldMap, countryNames);
        nbviz.onDataChange();
    }
}(window.nbviz = window.nbviz || {}));