// Sample job data (replace this with actual job data)
const jobs = [
    { title: 'Job 1', education: 'bachelor', jobType: 'full_time', salary: 50000, experience: 'entry_level' },
    { title: 'Job 2', education: 'master', jobType: 'part_time', salary: 40000, experience: 'mid_level' },
    { title: 'Job 3', education: 'high_school', jobType: 'full_time', salary: 60000, experience: 'senior' },
    // Add more job data here
  ];
  
  // Function to display job listings based on filters
  function displayJobs(filteredJobs) {
    const jobListings = document.getElementById('jobListings');
    jobListings.innerHTML = '';
  
    filteredJobs.forEach(job => {
      const jobDiv = document.createElement('div');
      jobDiv.textContent = `Title: ${job.title}, Education: ${job.education}, Job Type: ${job.jobType}, Salary: $${job.salary}, Experience: ${job.experience}`;
      jobListings.appendChild(jobDiv);
    });
  }
  
  // Function to apply filters and display matching jobs
  function applyFilters() {
    const educationFilter = document.getElementById('educationFilter').value;
    const jobTypeFilter = document.getElementById('jobTypeFilter').value;
    const minSalary = document.getElementById('minSalary').value;
    const maxSalary = document.getElementById('maxSalary').value;
    const experienceFilter = document.getElementById('experienceFilter').value;
  
    const filteredJobs = jobs.filter(job => {
      const meetsEducation = educationFilter === '' || job.education === educationFilter;
      const meetsJobType = jobTypeFilter === '' || job.jobType === jobTypeFilter;
      const meetsSalary = (minSalary === '' || job.salary >= parseInt(minSalary)) && (maxSalary === '' || job.salary <= parseInt(maxSalary));
      const meetsExperience = experienceFilter === '' || job.experience === experienceFilter;
  
      return meetsEducation && meetsJobType && meetsSalary && meetsExperience;
    });
  
    displayJobs(filteredJobs);
  }
  
  // Function to reset filters and display all jobs
  function resetFilters() {
    document.getElementById('educationFilter').value = '';
    document.getElementById('jobTypeFilter').value = '';
    document.getElementById('minSalary').value = '';
    document.getElementById('maxSalary').value = '';
    document.getElementById('experienceFilter').value = '';
  
    displayJobs(jobs);
  }
  
  // Display all jobs initially
  displayJobs(jobs);
  