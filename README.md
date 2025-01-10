# Monitoring-and-Observability-for-Development-and-DevOps
https://www.coursera.org/learn/monitoring-and-observability-for-development-and-devops

## I. Introduction to Monitoring for Applications
- (1) Monitoring Basics
  ![image](https://github.com/user-attachments/assets/4f25f8d7-79ca-45fe-a3fb-c7d6667f075a)
  - evaluation of application
    ![image](https://github.com/user-attachments/assets/aff142b5-004f-4f1c-a105-1948a639c456)

  - types of monitoring
    - **system monitoring**
      ![image](https://github.com/user-attachments/assets/1ccca0e8-2165-47ab-af89-db756960a03f)
    - dependency monitoring
      ![image](https://github.com/user-attachments/assets/7156eff5-68a3-4472-8a94-4ae87186652a)
    - integration monitoring (monitor 3rd parties)
      ![image](https://github.com/user-attachments/assets/1e5370b5-578b-454c-891c-d99641c46d1a)
    - web performance monitoring
      ![image](https://github.com/user-attachments/assets/1000ea73-f4e6-4b9a-98e0-0812030253a1)
    - business activity monitoring (BAM)
      ![image](https://github.com/user-attachments/assets/88a8561b-312c-4e27-b792-dbedcec82420)
    - application performance monitoring (APM)
      ![image](https://github.com/user-attachments/assets/2be6d359-900b-40aa-af81-7d8ed72ae869)
      metrics used:
      ![image](https://github.com/user-attachments/assets/5038589a-b2c0-4466-8451-090a278cb175)

    - **real user monitoring (RUM)**
      ![image](https://github.com/user-attachments/assets/c52741bb-b030-4013-a085-fe3a1b4c7371)
    - **security monitoring**
      ![image](https://github.com/user-attachments/assets/7c0a0278-df6d-4763-a923-e83440613115)

  - Four Golden Signals of Monitoring
     ![image](https://github.com/user-attachments/assets/386b95c9-0d75-47b9-98ca-d08b25ea9c71)
     - latency (request and response)
       ![image](https://github.com/user-attachments/assets/9b710220-d2b2-41ae-bd5f-0bd7904c3d0d)
     ![image](https://github.com/user-attachments/assets/0e34a11e-32a8-4e19-8633-2d29ec463199)

- (2) Objectives of Monitoring
  - monitoring and evaluation difference
    ![image](https://github.com/user-attachments/assets/e19759de-b292-4ab3-9cdc-96b7e2c8807a)
    ![image](https://github.com/user-attachments/assets/3333ede0-7985-4aff-a4f4-bbc9434b0be4)

  - components of monitoring
    ![image](https://github.com/user-attachments/assets/712ce8e3-dc75-4814-9046-f8895b857e68)
    ![image](https://github.com/user-attachments/assets/0ecc86ee-3a38-4d7d-8ceb-4cfbd3ec8e94)

  - types of metrics in a monitoring system
    ![image](https://github.com/user-attachments/assets/9b39da75-474f-4100-93b4-5755002b3342)
    - host-based metrics
      ![image](https://github.com/user-attachments/assets/6df5aab7-b261-4608-a0fb-cd63a56c9b42)
    - application metrics
      ![image](https://github.com/user-attachments/assets/c0418c20-b777-4480-9951-d008f3dbf1e2)
    - network and connectivity metrics
      ![image](https://github.com/user-attachments/assets/0fb6f5ec-6c64-42b2-8fd8-1f6958fdfc10)
    - server pool metrics
      ![image](https://github.com/user-attachments/assets/20867e8f-0e7c-4682-91cb-9a792312dc34)
    - external dependency metrics
      ![image](https://github.com/user-attachments/assets/631dfe20-ad2d-40cd-b1e5-9d0fb3752728)

  - importance of monitoring
    ![image](https://github.com/user-attachments/assets/399da906-e629-4e91-b5f6-5a4e55bf1568)

  
## II. Monitoring Systems and Techniques
- (1) Implementing Monitoring
  - synthetic monitoring (active monitoring)
    - Real user monitoring(**RUM**) vs. synthetic monitroing(**SM**)
  - tools
    ![image](https://github.com/user-attachments/assets/eb025438-ed3d-48b6-bf23-9bcb85f98a77)
  - application monitoring
    ![image](https://github.com/user-attachments/assets/8c0d7613-3789-4aaa-b956-93034410df2e)
    - telemetry monitored (system data auto gathered for moinitoring)
  - **Prometheus** (open source monitoring and alerting solution)
      ![image](https://github.com/user-attachments/assets/b40db4cb-f82a-4b20-b112-38afc6d1b364)
    ![image](https://github.com/user-attachments/assets/4942a546-42ca-4ca0-9c85-63fa03738d64)

  - choosing the right application monitoring (**APM**) tool
    ![image](https://github.com/user-attachments/assets/a20e3218-2590-48c9-8511-280a99c5a889)
  - **Grafana** (corss-platform, open-source data **visualization and metrics analysis tool**)
 
- (2) Monitoring Techniques
  - using Visualization in Monitoring
    ![image](https://github.com/user-attachments/assets/e7d9d2ce-c48c-493d-8a3a-092ac441d8be)
    ![image](https://github.com/user-attachments/assets/c4957430-11b5-439a-868b-52ae3fb35164)
  - alerting in monitoring
    ![image](https://github.com/user-attachments/assets/75f65afe-4ccf-4e04-a60e-c2d4b787d7a8)
    ![image](https://github.com/user-attachments/assets/77fb8dc1-f2be-4e38-9bfa-5dcfd4f93891)
    ![image](https://github.com/user-attachments/assets/69f74298-4416-46ca-863c-00ed50a900af)


## III. Methodologies and Tools in Logging
- (1) Logging
  ![image](https://github.com/user-attachments/assets/1442c714-6b6b-4ee6-bfa4-bd932ff1235e)
  
  

    


- (2) Logging Implementation
  ![image](https://github.com/user-attachments/assets/570b03d8-11d1-4154-8640-9dcd2c0e4314)

  - log storage
    ![image](https://github.com/user-attachments/assets/23b9b40c-0598-46bd-af61-b638d5611e2d)
  - log analyzer (e.g. CloudVyzor LogPad)
    
- (3) Introduction to Mezmo

## IV. Observability and Concepts
- (1) Observability
- (2) Tracing using Open Telemetry


## V. Final Assessment
