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