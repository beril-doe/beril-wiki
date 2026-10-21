// esbuild's text loader: the client bundle is imported as a string.
declare module "*.txt" {
  const text: string
  export default text
}
