const appEnv = process.env.REACT_APP_APP;

const constants = {};

for (const [key, value] of Object.entries(process.env)) {
  if (key.startsWith(`REACT_APP_${appEnv}_`)) {
    const constantName = key.replace(`REACT_APP_${appEnv}_`, "");
    constants[constantName] = value;
  }
}

export default constants;
