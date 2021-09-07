My Projects:

<table>
  <thead>
    <tr>
      <th>Project</th>
      <th>Client</th>
      <th>Spent</th>
      <th>Budget</th>
      <th>Remaining</th>
    </tr>
  </thead>
  <tbody>
    % for project in projects:
    <tr>
      <td>${project['project_name']}</td>
      <td>${project['client_name']}</td>
      <td>${project['budget_spent']}</td>
      <td>${project['budget']}</td>
      <td>${project['budget_remaining']}</td>
    </tr>
    % endfor
  </tbody>
</table>
