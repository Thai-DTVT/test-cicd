<?php
    require_once('config/db.php');
    
    function display_data(){
        global $conn;
        $sql = "SELECT * FROM infor_news ORDER BY id DESC limit 10";
        $result = $conn->query($sql);

        return $result;
    }
    
    function display_data_limit($limit){
        global $conn;
        $sql = "SELECT * FROM infor_news ORDER BY id DESC limit $limit  " ;
        
        $result = $conn->query($sql);

        return $result;
    } 
    //
    
    //

    function display_data_filter_by_date($date_from, $date_to, $limit){
        global $conn;
        $sql = "SELECT * FROM infor_news where created_at between '".$date_from."' and '".$date_to."' limit $limit  ";
        $result = $conn->query($sql);

        return $result;
    }
    function display_data_filter_by_tonghop($categoty,$provines,$date_from, $date_to, $limit){
        global $conn;
        $sql = "SELECT * FROM infor_news where categoty LIKE '%".$categoty."%' and provines LIKE '%".$provines."%' and created_at between '".$date_from."' and '".$date_to."' limit $limit  ";
        $result = $conn->query($sql);

        return $result;
    }

    function display_data_filter_by_categoty($categoty,$provines, $limit){

        global $conn;
        $sql = "SELECT * FROM infor_news where categoty LIKE '%".$categoty."%' and provines LIKE '%".$provines."%'  limit $limit ";

        $result = $conn->query($sql);  
        return $result;
    }
    
    function display_data_all(){
        
        global $conn;
        $sql = "SELECT * FROM infor_news " ;
        
        $result = $conn->query($sql);

        return $result;
    }
    
?>
