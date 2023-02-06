var app = new Vue({ 
    el: '#app',
    delimiters: ['[[', ']]'],
    data() {
        return { 
            sort_order : 1,
            project_data_list: [],
            form :{
                search_box : ""
            },
            paginator : {
                per_page : 0,
                current_page : 1,
                num_pages : 0
            },
            overview_project_id : 0,
            data_loading : true,
            zero_project : true,
            sort_editing : false
         }
    },
    mounted(){
        fetch('/spl/api/project_data/')
        .then((response) => {
            if (response.ok) {
                return response.json();
              }
              throw new Error('Connection Error');
        })
        .then((data) => {
            this.project_data_list = data;
            this.project_data_list.forEach(project => {
                                    project.ranking = [project.current_ranking, project.current_ranking]; // [old, new]
                                    project.days = project.time_duration.day + project.time_duration.month*30 + + project.time_duration.year*365; 
                                    project.total_participants = project.num_participant.airforce + project.num_participant.not_airforce;

                                    project.set_ranking = function(new_rank) { this.ranking[2] = new_rank; }
                                });
            if(this.project_data_list.length > 0){
                this.set_pagination();
                this.overview_project_id = this.project_data_list[0].id;
                this.zero_project = false;
            }
            this.data_loading = false;            
        })
        .catch((error) => {
            console.log(error)
        });
    },
    methods : {
        set_pagination(per_page = 20){
            this.paginator.per_page = per_page;
            this.paginator.num_pages = Math.ceil(this.project_data_list.length / this.paginator.per_page);
        },
        sort_data(key){
            this.sort_order = -1 * this.sort_order;
            this.project_data_list.sort((a, b) => this.sort_order * (a[key] - b[key]) );
        },
        reset_ranking(){            
            this.project_data_list.forEach(pm => pm.ranking[1] = pm.ranking[0]); 
            this.sort_editing = false;
        },
        test(x,prj)
        {
            console.log("x = ",x);
            console.log("prj = ",prj);
        },
        save_ranking(){            
            console.log(this.project_data_list);
            this.project_data_list.forEach(pm => {
                console.log(pm.ranking[0], pm.ranking[1]);
                pm.current_ranking = pm.ranking[0] = pm.ranking[1] = 5
            }); 
            this.sort_editing = false;
            console.log(this.project_data_list);
        },
        numberWithCommas(x) {
            return x.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
        }
    },
    computed :{
        display_projects() {
            if(this.form.search_box.length >= 3)
            {
                return this.project_data_list.filter((project)=>{ 
                    return project.name.includes(this.form.search_box) 
                            || project.project_category.includes(this.form.search_box)
                            || project.response_department.includes(this.form.search_box);
                }).slice((this.paginator.current_page - 1) * this.paginator.per_page, this.paginator.current_page * this.paginator.per_page);
            }
            return this.project_data_list.slice((this.paginator.current_page - 1) * this.paginator.per_page, this.paginator.current_page * this.paginator.per_page);
        },
        overview_project(){
            return this.project_data_list.find(project => project.id == this.overview_project_id);
        }
    },
    watch: {
        paginator: {
          handler(newValue) {
            this.set_pagination(parseInt(newValue.per_page));
            if(this.paginator.current_page > this.paginator.num_pages)
                this.paginator.current_page = this.paginator.num_pages
          },
          deep: true
        }
    }
});