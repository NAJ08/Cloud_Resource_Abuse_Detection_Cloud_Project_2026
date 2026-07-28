# Dataset Details

We are using two datasets for SentinelGraph because a single dataset doesn't cover both the network-level abuse signals and the identity/access signals that our graph model needs.

## Dataset 1 - CSE-CIC-IDS2018

- **Name:** CSE-CIC-IDS2018
- **Source:** Canadian Institute for Cybersecurity + Communications Security Establishment, hosted on AWS
- **URL:** https://www.unb.ca/cic/datasets/ids-2018.html
- **Size:** roughly 450 GB of raw PCAP/log data (10 days of traffic)
- **Records:** about 16.23 million labeled flow records
- **Features:** 80 per-flow features (CICFlowMeter-V3)
- **Data type:** tabular CSV, derived from raw PCAP
- **License:** free for research use, attribution required, no commercial redistribution
- **Why we use it:** covers the resource-abuse side - DoS, DDoS, botnet, brute force, infiltration. These patterns map to the tenant-resource edges in our graph.

**Preprocessing steps:**
- Merge the 10 daily CSV files
- Drop constant or near-duplicate columns
- Normalize numerical features
- Convert 15-class labels to binary (abuse / not abuse)
- Map source/destination IP-port pairs to synthetic tenant and resource node IDs

## Dataset 2 - CERT Insider Threat Dataset r4.2

- **Name:** CERT Insider Threat Dataset (Release r4.2)
- **Source:** Carnegie Mellon University CERT Division / Software Engineering Institute
- **URL:** https://kilthub.cmu.edu/articles/dataset/Insider_Threat_Test_Dataset/12841247
- **Size:** ~1000 simulated users, 1003 computers, Jan 2010 to May 2011 (17 months)
- **Records:** roughly 32.8 million event records. 70 users have malicious insider scenarios.
- **Features:** 4-10 fields per log type. After aggregation, around 20-50 engineered features per user session.
- **Data type:** multi-modal CSV logs - logon, file, email, device, http, psychometric, plus an LDAP org structure file
- **License:** research-use license from CMU CERT/SEI, must request access
- **Why we use it:** covers the identity/privilege-escalation side. User-role-resource relationships from LDAP become the node/edge structure for detecting lateral movement, which the network dataset alone can't capture.

**Preprocessing steps:**
- Join the 6 log files on user ID and timestamp
- Convert event streams into daily/session activity vectors per user
- Build the identity graph from the LDAP file (users to roles to resources)
- Align the malicious-user answer files to get ground-truth labels
- Handle the class imbalance (roughly 1:14 malicious to normal)

## Folder layout

```
dataset/
├── raw/        - original unmodified files
├── processed/  - cleaned data ready for model training
└── Dataset_Details.md
```

Note: raw dataset files are too large to commit directly. Store in S3 or use Git LFS.
