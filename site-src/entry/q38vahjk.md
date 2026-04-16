---
title: 'Agent Skills综述'
sidebar: false
---

::: info
[← 返回智能体](/agents)
:::

# Agent Skills综述

> Agent 领域系统性综述，适合建立全景认知

🔗 [原文链接](https://arxiv.org/abs/2602.12430) | @**：arXiv | 🇨🇳 | ⭐⭐⭐ 3 ⭐3 3/5 📅 2026-03-24

`2026-03-24` `gui` `safety` `agent` `research` `llm` `reinforcement-learning` `survey`

---

来源: https://arxiv.org/abs/2602.12430

[2602.12430] Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

      
  
  
  
  

  
  
  
    
      Skip to main content
      
      
        
          
        
            Learn about arXiv becoming an independent nonprofit.
        
          We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
          Donate
        
      

      

  
     &gt; cs &gt; arXiv:2602.12430
  

        
        

          
    
      
        
          
          Help | Advanced Search
        
        
          
            
              All fields
              Title
              Author
              Abstract
              Comments
              Journal reference
              ACM classification
              MSC classification
              Report number
              arXiv identifier
              DOI
              ORCID
              arXiv author ID
              Help pages
              Full text
            
          
        
        
        Search
      
    
  
     

      
        
          
          
            
              
              
              
            
          
          
            open search
            
              
                
                  
                  
                  
                  GO
                
              
            

            open navigation menu
            
              
                quick links
                
                    Login
                    Help Pages
                    About
                
              
            
          
        
      
    

    
      

    
    
-->

  
    
      Computer Science > Multiagent Systems
    

    
      arXiv:2602.12430 (cs)[Submitted on 12 Feb 2026 (v1), last revised 17 Feb 2026 (this version, v3)]
    Title:Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward
    Authors:Renjun Xu, Yang Yan            View a PDF of the paper titled Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward, by Renjun Xu and Yang Yan
    View PDF
    HTML (experimental)

    
            Abstract:The transition from monolithic language models to modular, skill-equipped agents marks a defining shift in how large language models (LLMs) are deployed in practice. Rather than encoding all procedural knowledge within model weights, agent skills -- composable packages of instructions, code, and resources that agents load on demand -- enable dynamic capability extension without retraining. It is formalized in a paradigm of progressive disclosure, portable skill definitions, and integration with the Model Context Protocol (MCP). This survey provides a comprehensive treatment of the agent skills landscape, as it has rapidly evolved during the last few months. We organize the field along four axes: (i) architectural foundations, examining the SKILL$.$md specification, progressive context loading, and the complementary roles of skills and MCP; (ii) skill acquisition, covering reinforcement learning with skill libraries, autonomous skill discovery (SEAgent), and compositional skill synthesis; (iii) deployment at scale, including the computer-use agent (CUA) stack, GUI grounding advances, and benchmark progress on OSWorld and SWE-bench; and (iv) security, where recent empirical analyses reveal that 26.1% of community-contributed skills contain vulnerabilities, motivating our proposed Skill Trust and Lifecycle Governance Framework -- a four-tier, gate-based permission model that maps skill provenance to graduated deployment capabilities. We identify seven open challenges -- from cross-platform skill portability to capability-based permission models -- and propose a research agenda for realizing trustworthy, self-improving skill ecosystems. Unlike prior surveys that broadly cover LLM agents or tool use, this work focuses specifically on the emerging skill abstraction layer and its implications for the next generation of agentic systems. Project repo: this https URL
    

    
    
      
          Subjects:
          
            Multiagent Systems (cs.MA); Artificial Intelligence (cs.AI)
                
          MSC classes:
          68T50
        
        
          ACM&nbsp;classes:
          I.2.11
        

          Cite as:
          arXiv:2602.12430[cs.MA]
        
        
          &nbsp;
          (or 
              arXiv:2602.12430v3[cs.MA] for this version)
          
        
        
          &nbsp;
                        https://doi.org/10.48550/arXiv.2602.12430
              
                
                Focus to learn more
              
              
              
                                  arXiv-issued DOI via DataCite
            
          
        
    
  

    
      Submission history From: Renjun Xu[view email][v1]
        Thu, 12 Feb 2026 21:33:25 UTC (214 KB)[v2]
        Mon, 16 Feb 2026 07:44:54 UTC (214 KB)[v3]
        Tue, 17 Feb 2026 09:08:50 UTC (214 KB)

  
  
    
      
      Full-text links:
      Access Paper:
      
  
View a PDF of the paper titled Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward, by Renjun Xu and Yang YanView PDFHTML (experimental)TeX Source
 
      
          
          view license
        
    
        
    Current browse context: cs.MA

  

      &lt;&nbsp;prev
    
    &nbsp; | &nbsp;    
      next&nbsp;&gt;
    
  
    new
     | 
    recent
     | 2026-02
  
    Change to browse by:
    
        cs
        cs.AI
    
  

    
      
        References &amp; Citations
        
          NASA ADSGoogle Scholar
          Semantic Scholar
        
        
      

    export BibTeX citation
    Loading...

    
        
            BibTeX formatted citation
            &times;
        
        
            loading...
        
        
            Data provided by: 
            
        
    

  Bookmark
    
  
  
    
  
  
  

  
    Bibliographic Tools
    
      Bibliographic and Citation Tools
      
        
          
            
              
              
              Bibliographic Explorer Toggle
            
          
          
            Bibliographic Explorer (What is the Explorer?)
          
        
        
          
            
              
              
              Connected Papers Toggle
            
          
          
            Connected Papers (What is Connected Papers?)
          
        
          
            
              
              
              Litmaps Toggle
            
          
          
            Litmaps (What is Litmaps?)
          
        
        
          
            
              
              
              scite.ai Toggle
            
          
          
            scite Smart Citations (What are Smart Citations?)
          
        
      
        
        
        
        
    

    
    Code, Data, Media
    
      Code, Data and Media Associated with this Article
      
        
          
            
              
              
              alphaXiv Toggle
            
          
          
            alphaXiv (What is alphaXiv?)
          
        

        
          
            
              
              
              Links to Code Toggle
            
          
          
            CatalyzeX Code Finder for Papers (What is CatalyzeX?)
          
        

        
          
            
              
              
              DagsHub Toggle
            
          
          
            DagsHub (What is DagsHub?)
          
        
  
        
          
            
              
              
              GotitPub Toggle
            
          
          
            Gotit.pub (What is GotitPub?)
          
        

        
          
            
              
              
              Huggingface Toggle
            
          
          
            Hugging Face (What is Huggingface?)
          
        

        
          
            
              
              
              Links to Code Toggle
            
          
          
            Papers with Code (What is Papers with Code?)
          
        

        
          
            
              
              
              ScienceCast Toggle
            
          
          
            ScienceCast (What is ScienceCast?)
          
        
      

      
      
      
      
      
      
      
      
    

      
      Demos
      
        Demos
        
          
            
              
                
                
                Replicate Toggle
              
            
            
              Replicate (What is Replicate?)
            
          
          
            
              
                
                
                Spaces Toggle
              
            
            
              Hugging Face Spaces (What is Spaces?)
            
          
          
            
              
                
                
                Spaces Toggle
              
            
            
              TXYZ.AI (What is TXYZ.AI?)
            
          
        
        
        
        
      
      
      Related Papers
      
        Recommenders and Search Tools
        
          
            
              
                
                
                Link to Influence Flower
              
            
            
              Influence Flower (What are Influence Flowers?)
            
          
          
            
              
                
                
                Core recommender toggle
              
            
            
              CORE Recommender (What is CORE?)
            
          
        
        
          
            Author
            Venue
            Institution
            Topic
          
          
            
            
            
            
          
        
        
        
      

      
      
        About arXivLabs
      
      
        
          
            arXivLabs: experimental projects with community collaborators
            arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
            Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
            Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
          
          
            
          
        
      

    

  
    Which authors of this paper are endorsers? |
    Disable MathJax (What is MathJax?)
    
  
  mathjaxToggle();

      
    

    
      
        
        
          
            
              
                About
                Help
              
            
            
              
                
                  contact arXivClick here to contact arXiv
                   Contact
                
                
                  subscribe to arXiv mailingsClick here to subscribe
                   Subscribe
                
              
            
          
        
        
        
        
          
            
              
                Copyright
                Privacy Policy
              
            
            
              
                Web Accessibility Assistance
                
                  
                    arXiv Operational Status
