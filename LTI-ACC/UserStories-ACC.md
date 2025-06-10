# Generación de historias de usuario y tickets de trabajo.

https://claude.ai/public/artifacts/a90dea1b-cc99-4bdc-b5c3-1e421de1615b

He comenzado usando Claude Sonnet 4 con el siguiente prompt:

```markdown
<LTI-ACC.md>

Given this document, list top 2 user stories that should be built in first place to have a MVP working as soon as possible. 

List only the name of the user stories.
```

Y he obtenido:

```markdown
Based on the document, here are the top 2 user stories that should be built first for an MVP:

* AI-Powered Resume Screening and Candidate Ranking
* Basic Job Posting and Application Management

These two user stories form the core foundation of any ATS system - the ability to post jobs, receive applications, and automatically screen/rank candidates using AI. This provides immediate value by addressing the primary pain point mentioned in the document (manual resume screening wastes 40+ hours/week) while establishing the basic workflow needed for any hiring process.
```

Tras esto, he usado el siguiente prompt para generar la primera historia de usuario:

```markdown
# IDENTITY and PURPOSE

You are an expert on writing concise, clear, and illuminating technical user stories for new features in complex software programs.

# OUTPUT INSTRUCTIONS

* Write the user story in a fashion recognised by other software stakeholders, including product, development, operations and quality assurance.
* Split the user stor into smaller, more manageable stories that still provide incremental value and can be delivered quickly
* Think about edge cases to be covered for rock solid behavior.

EXAMPLE USER STORY

```
Description
As a Highlight developer
I want to migrate email templates over to Mustache
So that future upgrades to the messenger service can be made easier
Acceptance Criteria
- Migrate the existing alerting email templates from the instance specific databases over to the messenger templates blob storage.
	- Rename each template to a GUID and store in it's own folder within the blob storage
	- Store Subject and Body as separate blobs
- Create an upgrade script to change the value of the Alerting.Email.Template local parameter in all systems to the new template names.
- Change the template retrieval and saving for user editing to contact the blob storage rather than the database
- Remove the database tables and code that handles the SQL based templates
- Highlight sends the template name and the details of the body to the Email queue in Service bus  
	- this is handled by the generic Email Client (if created already)
	- This email type will be added to the list of email types that are sent to the messenger service (switch to be removed once all email templates are completed)  
- Include domain details as part of payload sent to the messenger service
Note: ensure that Ops know when this work is being done so they are aware of any changes to existing templates
```
# OUTPUT INSTRUCTIONS
- Write the user story according to the structure above.  
- That means the user story should be written in a simple, bulleted style, not in a grandiose, conversational or academic style.
# OUTPUT FORMAT
- Output a full, user story about the content provided using the instructions above.
- The structure should be: Description, Acceptance criteria 
- Write in a simple, plain, and clear style, not in a grandiose, conversational or academic style.
- Use absolutely ZERO cliches or jargon or journalistic language like "In a world…", etc.
- Do not use cliches or jargon.
- Do not include common setup language in any sentence, including: in conclusion, in closing, etc.
- Do not output warnings or notes—just the output requested.

# INPUT:

**AI-Powered Resume Screening and Candidate Ranking**
```

Obteniendo el siguiente artefacto:

```markdown
# User Story: AI-Powered Resume Screening and Candidate Ranking

## Description
As a recruiter
I want the system to automatically parse, screen, and rank resumes using AI
So that I can reduce manual review time by 80% and focus on the highest quality candidates

## Acceptance Criteria

### Resume Parsing Engine
- Parse uploaded resume files in PDF, DOC, DOCX formats
- Extract structured data including contact information, work experience, education, skills, and certifications
- Handle parsing errors gracefully and flag unparseable resumes for manual review
- Store parsed data in standardized candidate profile format
- Support resume parsing in under 10 seconds per document

### AI Scoring Algorithm
- Generate overall candidate score (0-100) based on job requirements matching
- Calculate skill match score comparing candidate skills to job requirements
- Evaluate experience relevance score based on work history alignment
- Assign confidence level to each score component
- Store scoring rationale and reasoning for transparency

### Candidate Ranking System
- Rank all candidates for a job posting by overall AI score
- Display candidates in ranked order on recruiter dashboard
- Show score breakdown (skill match, experience, overall) for each candidate
- Allow manual override of AI rankings when needed
- Update rankings automatically when new applications are received

### Job Requirements Integration
- Link AI scoring to specific job posting requirements
- Weight scoring based on required vs preferred qualifications
- Handle technical skills matching with proficiency levels
- Support years of experience requirements in scoring algorithm
- Account for education requirements in overall scoring

### Edge Cases and Error Handling
- Handle corrupted or password-protected resume files
- Process resumes with non-standard formatting or layouts
- Manage duplicate candidate applications across multiple jobs
- Handle missing or incomplete resume information gracefully
- Support resumes in multiple languages (initially English only)
- Process batch uploads of multiple resumes simultaneously

### Performance Requirements
- Process single resume in under 10 seconds end-to-end
- Support concurrent processing of up to 50 resumes
- Maintain 99% uptime for parsing and scoring services
- Store AI model versioning for score reproducibility
- Log all parsing and scoring activities for audit purposes

### Integration Points
- Connect to job posting data for requirement matching
- Store results in candidate profile database
- Trigger notifications to recruiters for high-scoring candidates
- Provide API endpoints for future mobile app integration
- Support webhook notifications for real-time updates
```


Tras esto, he usado el siguiente prompt para generar la primera historia de usuario:

```markdown
# IDENTITY and PURPOSE

You are an expert on writing concise, clear, and illuminating technical user stories for new features in complex software programs.

# OUTPUT INSTRUCTIONS

* Write the user story in a fashion recognised by other software stakeholders, including product, development, operations and quality assurance.
* Split the user stor into smaller, more manageable stories that still provide incremental value and can be delivered quickly
* Think about edge cases to be covered for rock solid behavior.

EXAMPLE USER STORY

```
Description
As a Highlight developer
I want to migrate email templates over to Mustache
So that future upgrades to the messenger service can be made easier
Acceptance Criteria
- Migrate the existing alerting email templates from the instance specific databases over to the messenger templates blob storage.
	- Rename each template to a GUID and store in it's own folder within the blob storage
	- Store Subject and Body as separate blobs
- Create an upgrade script to change the value of the Alerting.Email.Template local parameter in all systems to the new template names.
- Change the template retrieval and saving for user editing to contact the blob storage rather than the database
- Remove the database tables and code that handles the SQL based templates
- Highlight sends the template name and the details of the body to the Email queue in Service bus  
	- this is handled by the generic Email Client (if created already)
	- This email type will be added to the list of email types that are sent to the messenger service (switch to be removed once all email templates are completed)  
- Include domain details as part of payload sent to the messenger service
Note: ensure that Ops know when this work is being done so they are aware of any changes to existing templates
```
# OUTPUT INSTRUCTIONS
- Write the user story according to the structure above.  
- That means the user story should be written in a simple, bulleted style, not in a grandiose, conversational or academic style.
# OUTPUT FORMAT
- Output a full, user story about the content provided using the instructions above.
- The structure should be: Description, Acceptance criteria 
- Write in a simple, plain, and clear style, not in a grandiose, conversational or academic style.
- Use absolutely ZERO cliches or jargon or journalistic language like "In a world…", etc.
- Do not use cliches or jargon.
- Do not include common setup language in any sentence, including: in conclusion, in closing, etc.
- Do not output warnings or notes—just the output requested.

# INPUT:

**Basic Job Posting and Application Management**
```

Obteniendo el siguiente artefacto:

```markdown
# User Story: Basic Job Posting and Application Management

## Description
As a hiring manager
I want to create job postings and manage candidate applications
So that I can collect and track candidates through the hiring process

## Acceptance Criteria

### Job Posting Creation
- Create new job posting with title, description, department, location, and salary range
- Define required skills with proficiency levels and years of experience
- Set job type (full-time, part-time, contract, remote)
- Add custom screening questions for applicants
- Save job posting as draft or publish immediately
- Duplicate existing job postings to create similar roles

### Job Posting Management
- Edit existing job postings and update posted versions
- Set job posting expiration dates and auto-close functionality
- Pause and resume job postings without losing applications
- Archive closed positions while preserving application data
- Track job posting views and application conversion rates
- Assign multiple hiring managers to single job posting

### Application Submission
- Allow candidates to apply through public job posting page
- Collect resume file upload (PDF, DOC, DOCX formats)
- Capture cover letter text or file upload
- Present custom screening questions defined in job posting
- Validate required fields before submission
- Send confirmation email to candidate after successful application

### Application Management
- Display all applications for each job posting in organized list
- Show application status (new, reviewed, interviewed, rejected, hired)
- Allow bulk status updates for multiple applications
- Filter applications by status, submission date, or candidate source
- Search applications by candidate name or email
- Export application data to CSV for external analysis

### Application Workflow
- Move applications through predefined stages (screening, interview, offer)
- Track status change history with timestamps and user attribution
- Send automated status update emails to candidates
- Set reminder notifications for hiring managers on pending applications
- Prevent accidental application deletion with confirmation prompts
- Support application withdrawal by candidates

### Edge Cases and Error Handling
- Handle duplicate applications from same candidate for same job
- Process applications when job posting reaches maximum limit
- Manage applications when job posting is deleted or archived
- Handle large resume file uploads with size and format validation
- Process special characters in candidate names and international addresses
- Support candidates applying without creating user accounts
- Validate email addresses and prevent spam applications

### Data Management
- Store all application data in secure database with audit logs
- Maintain data retention policies for closed positions
- Support GDPR compliance with candidate data deletion requests
- Track application source (direct, job board, referral)
- Link applications to specific job posting versions
- Generate application reports for hiring analytics
```

Con estos artefactos obtenidos, he utilizado el primer user story para generar los tickets de trabajo en Github usando Github Copilot y el MCP de Github.

He usado el siguiente prompt en modo "Ask":

```markdown
Given this documentation #file:LTI-ACC.md and the following user story #file:US-1.md, make me a proposal of technical tasks that have to be done to get the user story completed.
```

Y he obtenido la siguiente propuesta:

-------

# Technical Tasks for AI-Powered Resume Screening and Candidate Ranking

## 1. Infrastructure Setup

### Database Implementation
- Create database tables for candidate profiles, parsed resumes, and scoring results
- Implement data models for job requirements and skills matching
- Set up version control for AI model tracking

### Cloud Infrastructure
- Configure scalable cloud services for concurrent processing
- Set up document storage for resume files
- Implement caching layer for performance optimization

## 2. Resume Parsing Service

### Document Processing
````python
class ResumeParser:
    def parse_document(self, file):
        """
        Parse resume documents in various formats
        Returns structured data object
        """
````

### Data Extraction
- Implement PDF parsing module
- Implement DOC/DOCX parsing module
- Create structured data extraction pipeline
- Build validation layer for extracted data

## 3. AI Model Development

### Scoring Algorithm
````python
class CandidateScorer:
    def calculate_score(self, candidate_profile, job_requirements):
        """
        Generate candidate scores based on requirements matching
        Returns score object with breakdown
        """
````

### Machine Learning Pipeline
- Develop skill matching model
- Implement experience evaluation algorithm
- Create education requirements matcher
- Build confidence score calculator

## 4. API Development

### RESTful Endpoints
````python
@app.route('/api/v1/resumes/parse', methods=['POST'])
def parse_resume():
    """
    Handle resume upload and parsing
    Returns parsed profile data
    """

@app.route('/api/v1/candidates/score', methods=['POST'])
def score_candidate():
    """
    Calculate candidate score for job
    Returns detailed scoring breakdown
    """
````

## 5. Frontend Implementation

### Dashboard Components
````typescript
interface CandidateRankingProps {
    jobId: string;
    candidates: Candidate[];
}

const CandidateRanking: React.FC<CandidateRankingProps> = ({ jobId, candidates }) => {
    // Component implementation
}
````

### User Interface Features
- Build candidate ranking display
- Implement score breakdown visualization
- Create manual override controls
- Design error handling notifications

## 6. Integration Features

### Notification System
````typescript
class NotificationHandler {
    async sendHighScoreAlert(candidateId: string, score: number): Promise<void> {
        // Implementation
    }
}
````

### Webhook Support
````typescript
interface WebhookConfig {
    url: string;
    events: string[];
}
````

## 7. Testing Requirements

### Unit Tests
````python
def test_pdf_parsing():
    """Test PDF resume parsing"""

def test_skill_extraction():
    """Test skill extraction accuracy"""
````

### Integration Tests
- End-to-end resume processing tests
- Performance testing under load
- API endpoint testing
- Error handling verification

## 8. Documentation

### Technical Documentation
- API documentation
- Database schema documentation
- System architecture diagrams
- Deployment guides

### User Documentation
- Admin guide for system configuration
- User guide for recruiters
- Troubleshooting documentation

## 9. Monitoring and Logging

### Monitoring Setup
````yaml
metrics:
  - name: resume_processing_time
    type: gauge
    labels:
      - format
      - status
````

### Logging Implementation
- Set up structured logging
- Implement audit trail logging
- Create error tracking system
- Configure performance monitoring

## 10. Security Implementation

### Data Protection
- Implement encryption for stored resumes
- Set up secure file handling
- Configure access control
- Implement data retention policies

These tasks should be prioritized based on dependencies and team capacity. I recommend starting with infrastructure and core parsing features, then moving to AI implementation and frontend development.

------

Tras esto, he cambiado al modo Agente y le he solicitado que cree cada una de las tareas como issue de GitHub:

```
I want you to #create_issue in Github in #githubRepo kasappeal/AI4Devs-design-2-RO-1 for every task. Provide all the context that would help developers in addition to the technnical work to be done. Use links between issues or documents if needed. Start from the beggining.
```

Y [creó las tareas](https://github.com/kasappeal/AI4Devs-design-2-RO-1/issues)...aunque necesitó un poco de ayuda porque [al principio las creó que en repo que no era](https://github.com/LIDR-academy/AI4Devs-design-2-RO-1/issues?q=is%3Aissue%20state%3Aclosed).