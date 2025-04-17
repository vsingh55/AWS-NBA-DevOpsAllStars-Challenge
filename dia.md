## Architecture Diagram  
```mermaid  
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#FF9900', 'clusterBkg': '#f6f6f6'}}}%%
graph TD
    %% ========== Initial Setup Block ==========
    subgraph setup["Initial Setup"]
        A[Import Libraries] --> B[Load .env File]
        B --> C[Configure AWS<br>Region: ap-south-1<br>Bucket: bucket-sports-analytics...]
        style A fill:#4CAF50,color:white
        style B fill:#4CAF50,color:white
        style C fill:#4CAF50,color:white
    end
    
    %% ========== AWS Clients Block ==========
    subgraph clients["AWS Service Clients"]
        D[[Create S3 Client]] 
        E[[Create Glue Client]]
        F[[Create Athena Client]]
        style D fill:#FF9900,color:white
        style E fill:#FF9900,color:white
        style F fill:#FF9900,color:white
    end
    
    %% ========== S3 Operations Block ==========
    subgraph s3["Amazon S3 Processes"]
        G[/"Create S3 Bucket<br>(Versioning Enabled)"/]
        H[/"Upload Data<br>Format: JSON Lines<br>Path: raw-data/nba_players.jsonl"/]
        style G fill:#FF9900,color:white
        style H fill:#FF9900,color:white
    end
    
    %% ========== Data Processing Block ==========
    subgraph data["Data Processing"]
        I[("Fetch NBA Data<br>From sportsdata.io API")]
        J[("Convert to JSONL Format<br>(Line-delimited JSON)")]
        style I fill:#2196F3,color:white
        style J fill:#2196F3,color:white
    end
    
    %% ========== Glue Operations Block ==========
    subgraph glue["AWS Glue Processes"]
        K[["Create Database<br>glue-nba-data-lake"]]
        L[["Define Schema<br>PlayerID:int, FirstName:string,..."]]
        M[["Create Table<br>nba_players<br>Location: s3://bucket/raw-data"]]
        style K fill:#FF9900,color:white
        style L fill:#FF9900,color:white
        style M fill:#FF9900,color:white
    end
    
    %% ========== Athena Operations Block ==========
    subgraph athena["Amazon Athena Setup"]
        N[["Configure Output Location<br>s3://bucket/athena-results"]]
        O[["Create Database<br>nba_analytics"]]
        style N fill:#FF9900,color:white
        style O fill:#FF9900,color:white
    end
    
    %% ========== Workflow Connections ==========
    setup --> clients
    clients --> s3
    clients --> data
    data -->|Processed Data| s3
    s3 -->|Metadata| glue
    glue -->|Table Definition| athena
    
    classDef aws fill:#FF9900,color:white;
    classDef setup fill:#4CAF50,color:white;
    classDef data fill:#2196F3,color:white;


    ```

    [![](https://mermaid.ink/img/pako:eNqtVetuIjcUfhXLK4QUDVOYAbLMtitxCVnalEQlbdUuVWRmDLiZsae2h4Ql_O0D9BH7JD22KSRc2mxV_xj53L45_s7x8QrHIqE4wqXSinGmI7Qq6znNaDlC5QlRtOwhp_iBSEYmKVVgWY05QuVcsozIZVekQhr3N_1-q1Wtlj1rjdNCaSo79zNrm9q1ZxMyoS40tmtj1vRR71CDJKyHzY1pKrjuk4ylS2NrQ0rpM8uIfbKJ1-r5Y3nM1-t1qTTmM0nyObrtGTeESiX01Xahbwnj6Gap54KjUSxZrlEnFfH9Mx8XpoqJw8kg4uMYn53V_CPRZ2dj_IuLMCthksaagfm2s9NusYBgFluwwEcdI6DrnEpiItQelFntj9Z5kOVCanTFJhKKQsHzy4l8PxFahB76VQnuIc0y6iFJfyuo0spDidCULzwkFIDuoXYc6pUgCbrgCyYFzyjXaFtxh-8DAPrz9z9Q-2Zw983FTx4adtp3F8PezfVgeHsIq_QypaiNpixNozf1brvfqHqxKWu06YZj_p1X-VOe7IQjxDI-lcSeKvTRwAhKyyLWhaToRooFU8Aw47MjHHcdG11JiYb0fxyhbsqAjg0LI6D4Mi2A3DZcC05Onbu7OYe7E__1HORB2Wzqvs1kROWCxVTBRhf5keR7L5IfhahTxPdUbxrE7ivKNI-qEE7SpWbxkYa4cCjf56lpie_IA-oRTRzI16Pr4ZVtA0keKgnovzgE6L9Iw9BlEcw8cSgzUFX4hFiASkru6SHI5ctCWLb3YADh7h_O4SrRe1Uldv4Xn-nf_0z_y_-lMwxxlp-Gb0kxbQ2doY439QfHZZ_qeG6u7bOCwm225XRtYWB9Jg65HGyqIfiCwuzpC5kRvWsJC2F741QZPmyOHdRazX747zQNXuW_pclujk34YZFNqKQJgtS5G8bqYLrbQYwqlfdPtSc3PJzebq0-eDKX0WkNSVYZPlPCxurqT_aJcEr3jVOiVI9Orc_p4r_b83ZJnR6H-_42rdOkvcMenkmW4AhGIfVwRqGERsT2OR9j-8yPcQTbhE5JkeoxhkcUwnLCfxYi-ztSimI2x9GUpAqkIocf0x4j0JjZViuhIFR2RcE1jmr1ILQoOFrhRxw13_ph47wRNGu1t-etoBV4eImjSuiD2AjOg2rjvAnfsLH28Cf746oPlvVfEr2SJQ?type=png)](https://mermaid.live/edit#pako:eNqtVetuIjcUfhXLK4QUDVOYAbLMtitxCVnalEQlbdUuVWRmDLiZsae2h4Ql_O0D9BH7JD22KSRc2mxV_xj53L45_s7x8QrHIqE4wqXSinGmI7Qq6znNaDlC5QlRtOwhp_iBSEYmKVVgWY05QuVcsozIZVekQhr3N_1-q1Wtlj1rjdNCaSo79zNrm9q1ZxMyoS40tmtj1vRR71CDJKyHzY1pKrjuk4ylS2NrQ0rpM8uIfbKJ1-r5Y3nM1-t1qTTmM0nyObrtGTeESiX01Xahbwnj6Gap54KjUSxZrlEnFfH9Mx8XpoqJw8kg4uMYn53V_CPRZ2dj_IuLMCthksaagfm2s9NusYBgFluwwEcdI6DrnEpiItQelFntj9Z5kOVCanTFJhKKQsHzy4l8PxFahB76VQnuIc0y6iFJfyuo0spDidCULzwkFIDuoXYc6pUgCbrgCyYFzyjXaFtxh-8DAPrz9z9Q-2Zw983FTx4adtp3F8PezfVgeHsIq_QypaiNpixNozf1brvfqHqxKWu06YZj_p1X-VOe7IQjxDI-lcSeKvTRwAhKyyLWhaToRooFU8Aw47MjHHcdG11JiYb0fxyhbsqAjg0LI6D4Mi2A3DZcC05Onbu7OYe7E__1HORB2Wzqvs1kROWCxVTBRhf5keR7L5IfhahTxPdUbxrE7ivKNI-qEE7SpWbxkYa4cCjf56lpie_IA-oRTRzI16Pr4ZVtA0keKgnovzgE6L9Iw9BlEcw8cSgzUFX4hFiASkru6SHI5ctCWLb3YADh7h_O4SrRe1Uldv4Xn-nf_0z_y_-lMwxxlp-Gb0kxbQ2doY439QfHZZ_qeG6u7bOCwm225XRtYWB9Jg65HGyqIfiCwuzpC5kRvWsJC2F741QZPmyOHdRazX747zQNXuW_pclujk34YZFNqKQJgtS5G8bqYLrbQYwqlfdPtSc3PJzebq0-eDKX0WkNSVYZPlPCxurqT_aJcEr3jVOiVI9Orc_p4r_b83ZJnR6H-_42rdOkvcMenkmW4AhGIfVwRqGERsT2OR9j-8yPcQTbhE5JkeoxhkcUwnLCfxYi-ztSimI2x9GUpAqkIocf0x4j0JjZViuhIFR2RcE1jmr1ILQoOFrhRxw13_ph47wRNGu1t-etoBV4eImjSuiD2AjOg2rjvAnfsLH28Cf746oPlvVfEr2SJQ)